# Build the manager binary
FROM golang as builder

WORKDIR /workspace
# Copy the Go Modules manifests
COPY go.mod go.mod
COPY go.sum go.sum
# cache deps before building and copying source so that we don't need to re-download as much
# and so that source changes don't invalidate our downloaded layer
#set proxy
RUN export https_proxy=http://192.168.2.4:7890 http_proxy=http://192.168.2.4:7890 all_proxy=socks5://192.168.2.4:7890 &&
    go mod download

# Copy the go source
COPY cmd/ cmd/

# Build
RUN go build -o lamp cmd/main.go

# Use distroless as minimal base image to package the manager binary
# Refer to https://github.com/GoogleContainerTools/distroless for more details
FROM ubuntu
WORKDIR /
COPY --from=builder /workspace/lamp .

ENTRYPOINT ["/lamp"]
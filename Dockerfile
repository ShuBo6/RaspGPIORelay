FROM golang
RUN wget https://github.com/ShuBo6/RaspGPIORelay/archive/refs/heads/gin.zip
RUN unzip gin.zip
RUN cd cmd
RUN go build -o main main.go
RUN main
FROM balenalib/raspberry-pi-golang
RUN git clone https://github.com/ShuBo6/RaspGPIORelay.git
RUN cd RaspGPIORelay
RUN git checkout gin
RUN cd cmd
RUN go build -o main main.go
RUN main
from json import dumps,loads
from  zmq import Context,PULL
import socket


class main():
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port


        self.context=Context()
        self.socket=self.context.socket(PULL)
        self.socket.bind("tcp://*:{port}".format(port=port))

    def close(self):
        self.socket.close()
        self.context.term()
if __name__ =='__main__':
    host="127.0.0.1"
    port=50000

    soc=main(host, port)

    recv_data = soc.socket.recv_string()

    print(recv_data)



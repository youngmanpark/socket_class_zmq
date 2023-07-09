from json import dumps, loads
from zmq import Context, PUSH
import socket


class main():
    def __init__(self, host: str, port: int, limit: int = 1024):
        self.host=host
        self.port=port
        self.limit=limit

        self.context = Context()
        self.socket = self.context.socket(PUSH)


        self.socket.connect("tcp://{host}:{port}".format(host=host,port=port))

    def close(self):
        self.socket.disconnect("tcp://{host}:{port}".format(host=self.host, port=self.port))
        self.socket.close()
        self.context.term()
    #
    # def send(self, data: bytes) -> None:
    #     self.socket.send(data)
    # #
    # def send_String(self, data: str) -> None:
    #     bytes_data = data.encode()
    #     self.send(bytes_data)
    #
    # def send_json(self, data: dict) -> None:
    #     string_data = dumps(data)
    #     bytes_data = string_data.encode()
    #     self.send(bytes_data)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 50000
    data = 'My name is Darth Vador'
    soc = main(host, port)

    send_data = soc.socket.send_string(data)

    print(send_data)

    soc.close()
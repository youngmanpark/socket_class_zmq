from json import dumps, loads
import socket


class main():
    def __init__(self, host: str, port: int, limit: int = 1024):
        self.host=host
        self.port=port
        self.limit=limit

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)



        try:
            self.socket.connect((self.host, self.port))

        except Exception as e:
            print(e)
            self.socket.close()
            exit()

    def send_String(self, data: str) -> None:
        bytes_data = data.encode()
        self.send(bytes_data)

    def send_json(self, data: dict) -> None:
        string_data = dumps(data)
        bytes_data = string_data.encode()
        self.send(bytes_data)

    def send(self, data: bytes) -> None:
        self.socket.sendall(data)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 50000
    data = "hi"
    soc = main(host, port)

    send_data = soc.send_String(data)

    print(send_data)
from json import dumps,loads
import socket


class main():
    def __init__(self, host: str, port: int,limit:int=1024):
        self.host = host
        self.port = port
        self.limit=limit

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

        self.socket.listen()

        self.client_socket, self.client_addr = self.socket.accept()
        print("클라이언트 주소{addr}".format(addr=self.client_addr))



    def recv(self) -> bytes:
        return self.client_socket.recv(self.limit)


    def recv_string(self) -> str:
        bytes_data = self.recv()
        string_data = bytes_data.decode()
        return string_data


    def recv_jscon(self) -> dict:
        bytes_data = self.recv()
        dict_data = loads(bytes_data)
        return dict_data

if __name__ =='__main__':
    host="127.0.0.1"
    port=50000

    soc=main(host,port)

    recv_data=soc.recv_string()

    print(recv_data)


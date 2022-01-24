import socket


class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def request_second(self, name_file):
        """"Клиент отправляет запрос(имя файла) на сервер. В ответ получает
            данные(текст) из этого файла"""
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((self.server_host, self.server_port))
        print("Connected to {} port {}".format(self.server_host, self.server_port))
        print(f"Send filename: {name_file}")
        data_send = name_file.encode("utf-8")
        client_sock.sendall(data_send)
        response = client_sock.recv(2048).decode("utf-8")
        print("Text from file:")
        print(response)
        client_sock.close()


host = "127.0.0.1"
port = 6985
file_name = "filename.txt"
request_one = Client(host, port)

if __name__ == '__main__':
    request_one.request_second(file_name)


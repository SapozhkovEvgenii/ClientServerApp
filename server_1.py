import socket
import os.path


class LocalServer:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def server_sock(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((self.server_host, self.server_port))
        server_sock.listen(5)
        return server_sock


class ServerRun(LocalServer):
    def server_run_1(self):
        """Сервер принимает запрос от клиента(имя файла). В ответ отправляет
            данные(текст) из этого файла"""
        while True:
            connection, client_address = self.server_sock().accept()
            print(f"Connect from {client_address}")
            data = connection.recv(2048)
            data = data.decode("utf-8")
            print(f"Name file: {data}")
            file_path = os.path.isfile("./filename.txt")
            if file_path:
                with open(f'./{data}', 'r') as file:
                    file_data = file.read()
                    connection.sendall(file_data.encode("utf-8"))
            else:
                print("File not found")
                break
            connection.close()


host = "127.0.0.1"
port = 6985
local_server_1 = ServerRun(host, port)

if __name__ == '__main__':
    local_server_1.server_run_1()

# server.py

import socket
import threading
import colorama

from node.utils import colorstr

colorama.init()


class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.client_socket = None
        self.client_address = None
        self.connection_message = None

    def start(self):
        self.socket = socket.socket()
        print(colorstr("cyan", "Socket successfully created"))

        self.socket.bind((self.host, self.port))
        print(colorstr("cyan", f"Socket binded to {self.host}:{self.port}"))

        self.socket.listen(5)
        print(colorstr("cyan", "Socket is listening"))

        self.client_socket, self.client_address = self.socket.accept()
        print(colorstr("cyan", "bold", "Got connection from"), self.client_address)

        self.client_socket.send("Thank you for connecting".encode())

        self.start_recv(self.client_socket)

        self.start_send(self.client_socket)

    def connect(self):
        self.socket = socket.socket()
        print(colorstr("cyan", "Socket successfully created"))

        self.socket.connect((self.host, self.port))

        self.start_recv(self.socket)

        self.start_send(self.socket)

    def start_send(self, socket: socket.socket):
        while True:
            data = input()

            socket.send(data.encode())

            if data == "quit":
                break

    def recv(self, socket: socket.socket):
        while True:
            data = socket.recv(1024).decode()
            if not data:
                break

            if data == "quit":
                break
            
            print(colorstr("green", "Them:"), end=" ")
            print(colorstr("yellow", data))

        socket.close()

    def start_recv(self, socket: socket.socket):
        threading.Thread(target=self.recv, args=(socket,)).start()

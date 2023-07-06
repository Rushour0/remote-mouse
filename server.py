# main.py

from node import Node

def main():
    host = ""  # Use an empty string to listen on all available interfaces
    port = 12346

    server = Node(host, port)
    server.start()

if __name__ == "__main__":
    main()

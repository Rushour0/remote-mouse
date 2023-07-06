# main.py

from node import Node

def main():
    host = "127.0.0.1"  # Use an empty string to listen on all available interfaces
    port = 12346

    client = Node(host, port)
    client.connect()

if __name__ == "__main__":
    main()

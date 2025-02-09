import socket
import os
import time
import sys
BUFFER_SIZE = 1024

def handle_client(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode()
    response = request[::-1]
    time.sleep(3)
    client_socket.send(response.encode())
    client_socket.close()

def main(PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen()

    print(f"Multi-Process Server listening on port {PORT}")

    while True:
        print("Waiting for connection...")
        client_socket, _ = server_socket.accept()
        print(f"Connection from {client_socket.getpeername()}")
        pid = os.fork()
        if pid == 0:  # Child process
            server_socket.close()  # Child does not need server socket
            handle_client(client_socket)
            exit(0)
        else:
            client_socket.close()  # Parent closes client socket because client is being handled by child process.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        port = 8080
        main(port)
    else:
        try:
            port = int(sys.argv[1])
            main(port)
        except ValueError:
            print("Error: Port must be a valid integer")
            sys.exit(1)


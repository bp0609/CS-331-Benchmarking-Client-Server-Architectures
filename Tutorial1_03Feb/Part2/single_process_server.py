import socket
import time
import sys

BUFFER_SIZE = 1024

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    print(f"Single-Process Server listening on port {port}")

    server_socket.listen()
    while True:
        print("Waiting for connection...")
        client_socket, addr = server_socket.accept()        
        print(f"Connection from {addr}")
        request = client_socket.recv(BUFFER_SIZE).decode()
        response = request[::-1]
        time.sleep(3)
        client_socket.send(response.encode())

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

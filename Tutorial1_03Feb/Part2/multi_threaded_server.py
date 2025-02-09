import socket
import threading
import time
import sys
BUFFER_SIZE = 1024

def handle_client(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode()
    time.sleep(3)
    response = request[::-1]
    client_socket.send(response.encode())
    client_socket.close()

def main(PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen()

    print(f"Multi-Threaded Server listening on port {PORT}")

    while True:
        print("Waiting for connection...")
        client_socket, _ = server_socket.accept()
        print(f"Connection from {client_socket.getpeername()}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

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

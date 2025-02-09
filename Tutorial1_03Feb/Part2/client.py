import socket
import sys
SERVER_IP = "127.0.0.1"
BUFFER_SIZE = 1024


def main(SERVER_PORT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    message = "Bhavik"                  # OR Take input from user
    client_socket.send(message.encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(f"Server Response: {response}")

    print("Closing connection")
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        port = 8080
        main(port)
    else:
        try:
            port = int(sys.argv[1])
            main(port)
        except ValueError:
            print("Error: Port must be a valid integer")
            sys.exit(1)
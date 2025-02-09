import socket
import os

PORT = 8080
BUFFER_SIZE = 1024

def process_request(choice, input_data):

    if choice == "1":
        return input_data.swapcase()
    elif choice == "2":
        try:
            return str(eval(input_data))
        except:
            return "Invalid expression"
    elif choice == "3":
        return input_data[::-1]
    else:
        return "Invalid choice"

def handle_client(client_socket):
    while True:
        request = client_socket.recv(BUFFER_SIZE).decode()
        choice, input_data = request.split(":", 1)
        print(f"Request: {request}")
        if choice == "4":
            client_socket.send("Goodbye!".encode())
            client_socket.close()           # Close the connection with the client
            break
        response = process_request(choice, input_data)
        client_socket.send(response.encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen()

    print(f"Multi-Process Server listening on port {PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        pid = os.fork()
        if pid == 0:  # Child process
            server_socket.close()  # Child does not need server socket
            handle_client(client_socket)
            exit(0)
        else:
            client_socket.close()  # Parent closes client socket

if __name__ == "__main__":
    main()


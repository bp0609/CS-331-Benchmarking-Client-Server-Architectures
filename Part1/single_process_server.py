import socket

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

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    print(f"Single-Process Server listening on port {PORT}")

    # Build a persistent server
    server_socket.listen()
    while True:
        print("Waiting for a connection...")
        client_socket, addr = server_socket.accept()        # Make a connection and then go inside the loop and server that client only. If the client disconnects, then go back to the beginning of the loop and wait for a new client.
        print(f"Connection from {addr}")
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

if __name__ == "__main__":
    main()


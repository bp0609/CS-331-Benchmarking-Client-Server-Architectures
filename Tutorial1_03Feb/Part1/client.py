import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
BUFFER_SIZE = 1024

def display_menu():
    print("\nMenu:")
    print("1. Change case of string")
    print("2. Evaluate mathematical expression")
    print("3. Reverse a string")
    print("4. Exit")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    # Print if connection is successful or not
    print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "4":
            message = "4:exit"
            client_socket.send(message.encode())
            response = client_socket.recv(BUFFER_SIZE).decode()
            break

        data = input("Enter input: ")
        message = f"{choice}:{data}"
        client_socket.send(message.encode())

        response = client_socket.recv(BUFFER_SIZE).decode()
        print(f"Server Response: {response}")

    print(f"{response} received. Closing connection")
    client_socket.close()

if __name__ == "__main__":
    main()


import socket

def start_server():
    # Create a socket object and Server will listen on localhost and port 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Start listening for connections
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    try:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a message to the client
        message = "Hi from Server"
        print(f"Send message: {message}")
        client_socket.sendall(message.encode())

        # Receive a message from the client
        client_message = client_socket.recv(1024).decode()
        print(f"Received message from client: {client_message}")

        # Reply back to the client
        final_message = "Welcome Client 1!"
        print(f"Send back message to the client: {final_message}")
        client_socket.sendall(final_message.encode())

    finally:
        # Close the client connection
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()

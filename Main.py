import socket

def start_client():
    # Create a socket object and Connect to the server on localhost and port 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Receive the first message from the server
        server_message = client_socket.recv(1024).decode()
        print(f"Received message from server: {server_message}")

        # Send a single message to the server
        client_message = "Hi from Client 1"
        print(f"Send message: {client_message}")
        client_socket.sendall(client_message.encode())

        # Receive the final message from the server
        final_message = client_socket.recv(1024).decode()
        print(f"Received final message from server: {final_message}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()

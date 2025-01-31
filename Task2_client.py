import socket
import json

def start_client(client_id):
    # Create a socket object and connect to the server on localhost and port 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Receive the first message from the server
        server_message = client_socket.recv(1024).decode()
        print(f"Client {client_id} received message from server: {server_message}")

        # Send a message to the server
        if client_id == 2:  # Let Client 2 send JSON updates
            update_message = json.dumps({
                "light": "off",
                "door": "closed",
                "window": "closed"
            })
            print(f"Client {client_id} sends JSON update: {update_message}")
            client_socket.sendall(update_message.encode())
        else:
            client_message = f"Hi from Client {client_id}"
            print(f"Client {client_id} sends message: {client_message}")
            client_socket.sendall(client_message.encode())

        # Receive the final message from the server
        final_message = client_socket.recv(1024).decode()
        print(f"Client {client_id} received final message from server: {final_message}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    # Change the client_id for each client
    client_id = int(input("Enter client ID (e.g., 1, 2): "))
    start_client(client_id)

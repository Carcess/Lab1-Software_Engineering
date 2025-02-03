import socket
import threading
import json

# Function to handle a single client
def handle_client(client_socket, client_address, client_id):
    print(f"Connection established with Client {client_id} at {client_address}")

    # Send a unique message to the client
    welcome_message = f"Hi from Server to Client {client_id}"
    print(f"Send message: {welcome_message}")
    client_socket.sendall(welcome_message.encode())

    # Receive a message from the client
    client_message = client_socket.recv(1024).decode()
    print(f"Received message from Client {client_id}: {client_message}")

    # If the message is an update for the JSON file
    if client_message.startswith("{") and client_message.endswith("}"):
        try:
            # Parse the JSON update
            update_data = json.loads(client_message)

            # Update the JSON file
            with open("House.json", "w") as json_file:
                json.dump(update_data, json_file, indent=4)
                print("Updated House.json with new values:")
                print(update_data)

            # Notify the client that the update was successful
            client_socket.sendall(b"JSON file updated successfully!")

        except json.JSONDecodeError:
            # If the JSON format is incorrect, notify the client
            print("Failed to decode JSON from client.")
            client_socket.sendall(b"Invalid JSON format!")

    # Send a unique reply to the client
    final_message = f"Welcome Client {client_id}!"
    print(f"Send back message to Client {client_id}: {final_message}")
    client_socket.sendall(final_message.encode())

    # Close the connection with this client
    client_socket.close()

def start_server():
    # Create a socket object and server will listen on localhost and port 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  
    server_socket.bind(server_address)
    server_socket.listen(5)  # Allow up to 5 connections
    print("Server is waiting for connections...")

    # Create a JSON file for the "House"
    house_state = {
        "light": "on",
        "door": "open",
        "window": "open"
    }
    with open("House.json", "w") as json_file:
        json.dump(house_state, json_file, indent=4)

    client_id = 1
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_id))
        client_thread.start()
        client_id += 1

if __name__ == "__main__":
    start_server()

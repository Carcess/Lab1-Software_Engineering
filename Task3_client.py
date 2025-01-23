import socket
import json

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        # Send a JSON update to the server
        update_message = json.dumps({
            "light": "off",
            "door": "closed",
            "window": "closed"
        })
        print(f"Sending JSON update to server: {update_message}")
        client_socket.sendall(update_message.encode())

        # Receive acknowledgment from the server
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()

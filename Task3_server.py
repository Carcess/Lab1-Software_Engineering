import socket
import threading
import json
import tkinter as tk

# Function to handle a single client
def handle_client(client_socket):
    while True:
        try:
            # Receive a message from the client
            client_message = client_socket.recv(1024).decode()
            if not client_message:
                break

            print(f"Received message from client: {client_message}")
            
            # If the message is a JSON update
            if client_message.startswith("{") and client_message.endswith("}"):
                update_data = json.loads(client_message)

                # Update the JSON file
                with open("House.json", "w") as json_file:
                    json.dump(update_data, json_file, indent=4)
                    print("Updated House.json with new values:", update_data)

                # Update the graphical objects
                update_graphics(update_data)

            # Send an acknowledgment to the client
            client_socket.sendall(b"Update received and applied!")
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

# Function to update the graphical objects
def update_graphics(data):
    # Update light
    if data["light"] == "on":
        canvas.itemconfig(light, fill="yellow")
    else:
        canvas.itemconfig(light, fill="gray")

    # Update door
    if data["door"] == "open":
        canvas.itemconfig(door, fill="green")
    else:
        canvas.itemconfig(door, fill="red")

    # Update window
    if data["window"] == "open":
        canvas.itemconfig(window, fill="blue")
    else:
        canvas.itemconfig(window, fill="black")

# Function to start the server
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server is waiting for connections...")

    # Accept clients in a new thread
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Create a Tkinter window for graphical representation
root = tk.Tk()
root.title("House State")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw graphical objects
light = canvas.create_oval(50, 50, 150, 150, fill="yellow")  # Circle for light
door = canvas.create_polygon(200, 200, 250, 300, 150, 300, fill="green")  # Triangle for door
window = canvas.create_rectangle(300, 50, 350, 100, fill="blue")  # Square for window

# Start the server in a new thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Run the Tkinter main loop
root.mainloop()

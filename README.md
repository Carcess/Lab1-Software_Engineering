# Lab1-Software_Engineering
# README

## Overview
This project is a solution for **Lab 1** tasks, which involves implementing a client-server communication system using Python. The tasks include:

1. **Task 1**: Basic client-server communication.
2. **Task 2**: Extending the server to handle multiple clients and update a JSON file.
3. **Task 3**: Adding graphical elements (light, door, window) to the server that change based on client input.

---

## Task 1: Basic Client-Server Communication

### **Description**
- The task implements a simple client-server application where:
  1. The server sends a message to the client: `"Hi from Server"`.
  2. The client responds: `"Hi from Client 1"`.
  3. The server replies: `"Welcome Client 1!"`.

### **Files**
- `Task1_server.py`
- `Task1_client.py`

### **How to Run**
1. Start the server:
   ```bash
   python Task1_server.py
   ```
2. Run the client in another terminal:
   ```bash
   python Task1_client.py
   ```

### **Expected Output**
- **Server Output**:
  ```
  Server is waiting for a connection...
  Connection established with ('127.0.0.1', <port>)
  Send message: Hi from Server
  Received message from client: Hi from Client 1
  Send back message to the client: Welcome Client 1!
  ```
- **Client Output**:
  ```
  Received message from server: Hi from Server
  Send message: Hi from Client 1
  Received final message from server: Welcome Client 1!
  ```

---

## Task 2: Multi-Client Server and JSON File Update

### **Description**
- Extends the server to handle multiple clients using threading.
- Each client receives unique messages:
  - Client 1: `"Welcome Client 1!"`
  - Client 2: `"Welcome Client 2!"`
- Client 2 sends updates to a `House.json` file.

### **Files**
- `Task2_server.py`
- `Task2_client.py`
- `House.json` (initial state):
  ```json
  {
    "light": "on",
    "door": "open",
    "window": "open"
  }
  ```

### **How to Run**
1. Start the server:
   ```bash
   python Task2_server.py
   ```
2. Run multiple clients:
   ```bash
   python Task2_client.py
   ```
   Enter `1` for the first client and `2` for the second client.

### **Expected Output**
- **Server Output**:
  ```
  Server is waiting for connections...
  Connection established with Client 1 at ('127.0.0.1', <port>)
  Send message: Hi from Server to Client 1
  Received message from Client 1: Hi from Client 1
  Send back message to Client 1: Welcome Client 1!
  Connection established with Client 2 at ('127.0.0.1', <port>)
  Send message: Hi from Server to Client 2
  Received message from Client 2: {"light": "off", "door": "closed", "window": "closed"}
  Updated House.json with new values:
  {"light": "off", "door": "closed", "window": "closed"}
  Send back message to Client 2: Welcome Client 2!
  ```

- **Updated `House.json`**:
  ```json
  {
    "light": "off",
    "door": "closed",
    "window": "closed"
  }
  ```

---

## Task 3: Graphical Representation

### **Description**
- Adds graphical objects to the server for real-time updates:
  - **Circle** for `light` (yellow for "on", gray for "off").
  - **Triangle** for `door` (green for "open", red for "closed").
  - **Square** for `window` (blue for "open", black for "closed").
- The server updates these objects based on JSON data sent by the clients.

### **Files**
- `Task3_server.py`
- `Task3_client.py`
- `House.json`

### **How to Run**
1. Start the server:
   ```bash
   python Task3_server.py
   ```
   A window will open displaying the graphical objects.
2. Run the client:
   ```bash
   python Task3_client.py
   ```

### **Expected Behavior**
- The graphical objects on the server change in real-time based on the JSON updates sent by the client.
  - **Gray Circle**: Light is "off."
  - **Red Triangle**: Door is "closed."
  - **Black Square**: Window is "closed."

### **Sample Graphical Output**
- Initial State:
  - Yellow circle, green triangle, blue square.
- After Client 2 sends an update:
  - Gray circle, red triangle, black square.

---

## Submission Instructions
1. Ensure all files (`Task1_server.py`, `Task1_client.py`, `Task2_server.py`, `Task2_client.py`, `Task3_server.py`, `Task3_client.py`, `House.json`) are included.
2. Include this `README.md` file.
3. Test all tasks to ensure correctness.
4. Zip the project and upload it to Canvas.

---

## UML Diagrams
1. **Task 2 UML Class Diagram**:
   - Represents the server, client, and JSON handling.

2. **Task 3 UML Class Diagram**:
   - Adds graphical objects and their interaction with the server.


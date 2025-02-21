
import socket

class BlueICEIoT:
    
    """A simple TCP client that connects to a server and allows continuous messaging."""
    
    def __init__(self, host="128.175.213.230", port=65432):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """Connects to the TCP server."""
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
        return True

    def sendMessage(self, message):
        """Sends a message to the server and receives a response."""
        if not message:
            return

        try:
            self.client_socket.sendall(message.encode())

            if message.lower() == "exit":
                print("Closing connection...")
                self.client_socket.close()
                return "Disconnected"

            response = self.client_socket.recv(1024).decode()
            return response

        except Exception as e:
            print(f"Error sending message: {e}")
            return None

    def close(self):
        """Closes the client socket."""
        self.client_socket.close()
        print("Connection closed.")
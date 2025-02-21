
import socket
import time

class BlueICEIoT:

    """A simple TCP client that connects to a server and allows continuous messaging."""
    
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        self.sendMessage('spawn')

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
            start = time.time()
            self.client_socket.sendall(message.encode())

            if message.lower() == "exit":
                print("Closing connection...")
                self.client_socket.close()
                return "Disconnected"

            response = self.client_socket.recv(1024).decode()
            end = time.time()
            latency = (end - start) * 1000
            print(f"Msg latency is: {latency} ms.")
            # return response

        except Exception as e:
            print(f"Error sending message: {e}")
            return None

    def close(self):
        """Closes the client socket."""
        self.client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    server = BlueICEIoT()
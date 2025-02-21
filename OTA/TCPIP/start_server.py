
import socket
import carla

class BlueICEServer():

    def __init__(self):
        self.connect_2_SIM()
        self.start_server()
        

    def start_server(self, host="127.0.0.1", port=65432):
        self.host = host
        """Starts a TCP server that listens for messages and responds."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()

            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break  # Close connection if no data is received

                    msg = data.decode()

                    if msg.lower() == "spawn":
                        self.spawn('vehicle.lincoln.mkz_2017', 0)

                    print(f"Received from client: {data.decode()}")

                    response = "Message received!"
                    conn.sendall(response.encode())

    def connect_2_SIM(self):
        self.client = carla.Client('128.175.213.230', 2000)
        self.client.set_timeout(10.0)
        self.world = self.client.get_world()
        print("Connected to CARLA")
        self.spawn('vehicle.lincoln.mkz_2017', 0)

    def spawn(self, object, location):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = blueprint_library.find(object)
        spawn_points = self.world.get_map().get_spawn_points()
        vehicle = self.world.spawn_actor(vehicle_bp, spawn_points[location])


if __name__ == "__main__":
    server = BlueICEServer()

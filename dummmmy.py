class Device:
    def __init__(self, name, device_type, strength=5):
        self.name = name
        self.device_type = device_type
        self.strength = strength
        self.connections = []

    def __str__(self):
        return f"{self.device_type} ({self.name})"

class Network:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        if device.name in self.devices:
            print(f"Error: That name already exists.")
        else:
            self.devices[device.name] = device
            print(f"Successfully added {device.name}.")

    def connect_devices(self, device1, device2):
        if device1.name == device2.name:
            print(f"Error: Cannot connect device to itself.")
        elif device2.name not in self.devices:
            print(f"Error: Node not found.")
        elif device2 in device1.connections:
            print(f"Error: Devices are already connected.")
        else:
            device1.connections.append(device2)
            device2.connections.append(device1)
            print(f"Successfully connected.")

    def set_device_strength(self, device, strength):
        if device.device_type == "repeater":
            print("Error: A strength cannot be defined for a repeater.")
        elif not isinstance(strength, int) or strength < 0:
            print("Error: Invalid command syntax.")
        else:
            device.strength = strength
            print(f"Successfully defined strength.")

    def get_route(self, src_device, dest_device):
        if src_device.device_type == "repeater" or dest_device.device_type == "repeater":
            print(f"Error: Route cannot be calculated with a repeater.")
            return
        if dest_device not in src_device.connections:
            queue = [(src_device, [src_device.name])]
            visited = set()
            while queue:
                node, path = queue.pop(0)
                if node in visited:
                    continue
                visited.add(node)
                for connection in node.connections:
                    if connection == dest_device:
                        print(" -> ".join(path + [dest_device.name]))
                        return
                    queue.append((connection, path + [connection.name]))
            print(f"Error: Route not found!")
        else:
            print(f"{src_device.name} -> {dest_device.name}")

network=Network()
while True:
    command = input("> ").strip().split()
    if not command:
        print("Error: Invalid command syntax.")
        continue
    if command[0].upper() == "ADD":
        if len(command) != 3:
            print("Error: Invalid command syntax.")
        elif command[1].upper() == "COMPUTER":
            network.add_device(Device(command[2], "computer"))
        elif command[1].upper() == "REPEATER":
            network.add_device(Device(command[2], "repeater"))
        else:
            print("Error: Invalid command syntax.")

    elif command[0].upper() == "CONNECT":
        if len(command) != 3:
            print("Error: Invalid command syntax.")
        else:
            device1 = network.devices.get(command[1])
            device2 = network.devices.get(command[2])
            if device1 is None or device2 is None:
                print("Error: Node not found.")
            else:
                network.connect_devices(device1, device2)
    elif command[0].upper() == "SET_DEVICE_STRENGTH":
        if len(command) != 3:
            print("Error: Invalid command syntax.")
        else:
            device = network.devices.get(command[1])
            if device is None:
                print(f"Error: {command[1]} not found.")
            else:
                try:
                    network.set_device_strength(device, int(command[2]))
                except:
                    print("Error: Invalid command syntax.")
    elif command[0].upper() == "INFO_ROUTE":
        if len(command) != 3:
            print("Error: Invalid command syntax.")
        else:
            src_device = network.devices.get(command[1])
            dest_device = network.devices.get(command[2])
            if src_device is None:
                print("Error: Node not found.")
            elif dest_device is None:
                print("Error: Node not found.")
            else:
                network.get_route(src_device, dest_device)
    elif command[0].upper() == "QUIT":
        break
    else:
        print("Error: Invalid command syntax.")
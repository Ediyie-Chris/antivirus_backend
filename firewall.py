import socket

class SimpleFirewall:
    def __init__(self):
        self.allowed_ips = set() 
    def add_allowed_ip(self, ip):
        self.allowed_ips.add(ip)

    def remove_allowed_ip(self, ip):
        if ip in self.allowed_ips:
            self.allowed_ips.remove(ip)

    def is_allowed_ip(self, ip):
        return ip in self.allowed_ips

    def start(self, host, port):
        # Create a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Firewall started on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_ip = client_address[0]
            
            if self.is_allowed_ip(client_ip):
                print(f"Connection from {client_ip} allowed.")
                client_socket.send(b"Connection allowed.\n")
                client_socket.close()
            else:
                print(f"Connection from {client_ip} blocked.")
                client_socket.send(b"Connection blocked.\n")
                client_socket.close()

if __name__ == "__main__":
    firewall = SimpleFirewall()
    firewall.add_allowed_ip("127.0.0.1") 
    firewall.start("localhost", 8888)  

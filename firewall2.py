import socket

def connect_to_firewall(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        response = client_socket.recv(1024)
        print(response.decode())
    except ConnectionRefusedError:
        print("Connection refused")
    finally:
        client_socket.close()

if __name__ == "__main__":
    connect_to_firewall("localhost", 1234)

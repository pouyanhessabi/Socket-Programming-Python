import socket

# localhost and optional Port
HOST: str = "127.0.0.1"
PORT: int = 8000

# TCP connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        print("Couldn't find Server!")
        exit()
    message = input()
    s.sendall(message.encode())
    data = s.recv(1024).decode()
    print(data)

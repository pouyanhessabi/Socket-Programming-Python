import socket

HOST: str = "127.0.0.1"
PORT: int = 1000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        print("Couldn't find Server!")
        exit()
    message = "Hello"
    s.sendall(message.encode())
    data = s.recv(1024)
    data = data.decode()
    print("new data is " + data)
    s.close()
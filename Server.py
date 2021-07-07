import socket

HOST: str = "127.0.0.1"
PORT: int = 1000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Socket successfully created")
        s.bind((HOST, PORT))
        s.listen(10)
        while True:
            conn, address = s.accept()
            print(f"{address!r}")
            with conn:
                data = conn.recv(1024)
                data = data.decode()
                print("My data is: " + data)
                new_data = data + "World"
        # s.sendall(new_data.encode())
except socket.error as err:
    print("socket creation failed with error %s" % err)

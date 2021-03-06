import socket
from palindrome import check_if_palindrome

# to save received string and calculated palindrome
cache_dict = {}

# localhost and optional Port
HOST: str = "127.0.0.1"
PORT: int = 8000

try:
    # TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Socket successfully created")
        s.bind((HOST, PORT))
        s.listen(10)
        while True:
            conn, address = s.accept()
            # print(f"{address!r}")
            with conn:
                data = conn.recv(1024)
                data = data.decode()
                # print("My data is: " + data)
                if data in cache_dict:
                    response_bool = cache_dict[data]
                    # print("it was in cache")
                else:
                    palindrome_bool = check_if_palindrome(data)
                    if palindrome_bool:
                        # print(palindrome_bool)
                        response_bool = "True"
                    else:
                        response_bool = "False"
                    cache_dict[data] = response_bool
                conn.sendall(response_bool.encode())

except socket.error as err:
    print("socket creation failed with error %s" % err)

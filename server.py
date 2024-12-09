import socket
from Crypto.Util import number

import secrets
def generate_random_pair() -> tuple[int, int]:
    # (p, q)
    # p: large prime number
    # q: small rand number
    
    return (number.getPrime(2000), secrets.randbelow(10))

def main():
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 7001))
    server_socket.listen(3)
    while True:
        client, _ = server_socket.accept()
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...
    except Exception as e:
        raise e

        
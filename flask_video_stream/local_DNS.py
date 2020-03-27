import socket
import config
import time

UDP_IP = config.UDP_IP
UDP_PORT = config.UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(f"received message: {data.decode()}")

    if data:
        print(f"Hey! I got data from this address: {addr}")
        print("Let me resolve de DNS query")
        print("It is done. 127.0.0.1:8000. Give back to the client!")

        sock.sendto(b'127.0.0.1:8000', addr)
from flask import Flask
from flask import render_template
import config
import socket

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/config/')
def config_file():
    return str(config.POSTGRES_PORT)

@app.route('/hello/')
def hello():
    UDP_IP = config.UDP_IP
    UDP_PORT = config.UDP_PORT
    MESSAGE = "Hello, World!"

    print(f"UDP target IP: {UDP_IP}")
    print(f"UDP target port: {UDP_PORT}")
    print(f"message: {MESSAGE}")

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    ip, port = data.decode().split(':')
    TCP_IP = ip
    TCP_PORT = int(port)
    
    BUFFER_SIZE = 1024
    MESSAGE = "Please send me the video!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE.encode())

    f = open('static/downloadedvideo3.mp4', 'wb')
    data = s.recv(BUFFER_SIZE)

    while(data):
        print("Recieving........")
        f.write(data)
        data = s.recv(BUFFER_SIZE)
    f.close()
    s.close()

    print(f"received data: {data.decode()}")

    return render_template('play.html', video='/static/downloadedvideo3.mp4')
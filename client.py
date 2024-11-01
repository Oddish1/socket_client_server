import socket

HOST = 'localhost'
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # get the welcome message
    welcome = s.recv(1024).decode('utf-8')
    print('\n' + welcome)

    while True:
        message = input('>>> ')
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f'{data}')
        if message.lower() == 'quit':
            break
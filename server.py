import socketserver

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # send a welcome message to clients that connect
        welcome_message = 'Welcome to the server! Type "quit" to exit.'
        self.request.sendall(welcome_message.encode('utf-8'))

        while True:
            data = self.request.recv(1024).decode('utf-8')
            if not data:
                break # close the connection

            print(f'{self.client_address[0]}: {data}')
            
            # return 'Hi' when client sends 'Hello'
            if data.lower() == 'hello':
                self.request.sendall('Hi'.encode('utf-8'))
            # return 'Goodbye' otherwise
            elif data.lower() == 'quit':
                self.request.sendall('Goodbye'.encode('utf-8'))
                break # close the connection
            else:
                self.request.sendall('Goodbye'.encode('utf-8'))


HOST = 'localhost'
PORT = 9500

with socketserver.ThreadingTCPServer((HOST, PORT), RequestHandler) as server:
    print(f'Server started on {HOST}:{PORT}')
    server.serve_forever()
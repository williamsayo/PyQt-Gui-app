import socket
import threading

class Server():
    def __init__(self,host,port):
        self.clients = []
        self.users = {}
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen()

        while True:
            client, addr = self.server.accept()
            self.clients.append(client)
            print(f"{addr} connected to the server")

            client.send("username".encode('utf-8'))
            username = client.recv(1024).decode('utf-8')
            self.users[username] = addr
            
            print(f'Username of the client is {username}')

            self.broadcast_message(f'{username} joined the chat!',client)

            print(f'[Active connections] {len(self.clients)}')

            t2 = threading.Thread(target=self.client_handler , args=[client,username])
            t2.start()

    def client_handler(self,client,username):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.broadcast_message(message,client)

            except:
                self.remove_client(client,username)
                break

    def remove_client(self,client,username):    
        self.clients.remove(client)
        del(self.users[username])

        self.broadcast_message(f'{username} left the chat!',client)
        print(f'{username} left the server')
        
        client.close()

    def broadcast_message(self,message,client):
        for otherClient in self.clients:
            if otherClient != client:
                otherClient.send(f'{message}'.encode('utf-8'))

host = socket.gethostbyname(socket.gethostname())
port = 2424

if __name__ == "__main__":
    print(f'server started at {host} on port {port}')
    print(f'Server is running...')
    Server(host,port)
from socket import *
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class Server:
    def __init__(self):
        self.t0 = ''
        self.tn = ''
        self.trafego = 0
        self.tempo = [0, 0]
        self.client = None
        self.connection = None
    
    def send(self, msg):
        msg = ''
        self.client.send(bytes(msg, encoding='utf-8'))
    
    def receive(self):
        result = self.client.recv(1024)
        self.trafego+=1
        if len(result) > 0:
            return result
        else:
            raise Exception()
    
    def wait_client(self):
        print("Aguardando conexão...")
        self.client, addr = self.connection.accept()
        print("Herói conectado em {}:{}".format(addr[0], addr[1]))
        self.start()

    def start_server(self):
        port = 12000
        self.connection = socket(AF_INET, SOCK_STREAM)
        self.connection.bind(('', port))
        self.connection.listen(1)
        self.wait_client()

    def start(self):
        try:
            msg = self.receive()
            print(str(msg, 'utf-8'))
            self.t0 = datetime.now()
            while True:
                msg = self.receive()
                print(str(msg, 'utf-8'))
        except Exception:
            self.client.close()
            self.connection.close()
            print('Heroi saiu...')
            self.tn = datetime.now()
            self.tempo = [self.t0, self.tn]
            print(self.tn-self.t0)
            plt.plot(self.tempo, [0,self.trafego])
            plt.show()
            #self.tempo = [0, tn-t0]
            self.wait_client()


if __name__ == '__main__':
    Server().start_server()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
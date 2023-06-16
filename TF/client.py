from socket import *
from datetime import datetime
import time

hostname = gethostname() # change
serverName = gethostbyname(hostname) # change
serverPort = 12000
mission = True
x = datetime.now()

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#sentence = input('write START to start the game: ')
print('Gaming starting...')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
clientSocket.send(bytes(current_time,'utf-8'))
#time.sleep(5)
y = datetime.now()
while True:#x == datetime.now():
    #modifiedSentence = clientSocket.recv(1024)
    #print ('From server: ', modifiedSentence)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S\n")
    clientSocket.send(bytes('a','utf-8'))
    #x+=1
try:
    clientSocket.close()
except:
    sys.exit(1)
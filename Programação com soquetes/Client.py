from socket import *

hostname = gethostname()
serverName = gethostbyname(hostname)
serverPort = 12000
mission = True

while mission: 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    #sentence = input('write START to start the game: ')
    print('Gaming starting...')
    clientSocket.send(bytes('START','utf-8'))   
    while True:
        modifiedSentence = clientSocket.recv(1024)
        print ('From server: ', modifiedSentence)
        ms = modifiedSentence
        s = ms.decode("utf-8").split(';')

        if(s[0] == 'MONSTER_ATTACK'):
            #sentence = input('write something:')
            #clientSocket.send(bytes(sentence, 'utf-8'))
            print(s[1])
            clientSocket.send(bytes(s[1], 'utf-8'))
        elif(s[0] == 'TAKE_CHEST'):
            print('take it!')
            clientSocket.send(bytes('YES','utf-8'))
        elif(s[0] == 'BOSS_EVENT'):
            print('the power of friendship!')
            clientSocket.send(bytes('FIGHT','utf-8'))
        elif(s[0] == 'NOTHING_HAPPENED'):
            print('walking...')
            clientSocket.send(bytes('WALK','utf-8'))
        elif(s[0] == 'GAME_OVER'):
            try:
                clientSocket.close()
                print("it can't be real..")
                print(s[0],' SCORE: ',s[3])
                break # quando perder sai do loop para recriar o socket e estabelecer uma nova conexão e assim tentar de novo
            except error: # se der problema na conexão feche
                sys.exit(1)
        elif(s[0] == 'WIN'):
            clientSocket.close()
            print('Now.. peace finally')
            print(s[0],' SCORE: ', s[3])
            mission = False
            break # a missão acabou parabéns
        else:
            clientSocket.send(bytes('WALK','utf-8'))

clientSocket.close()
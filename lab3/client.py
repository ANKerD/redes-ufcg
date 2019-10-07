import sys
from socket import *
serverPort = int(sys.argv[1]) if len(sys.argv) > 1 else 9090

serverName = "localhost"

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input your command: ')

clientSocket.send(sentence.encode('utf-8'))

modifiedSentence = clientSocket.recv(1024)

print("From Server:", modifiedSentence.decode('utf-8'))

clientSocket.close()
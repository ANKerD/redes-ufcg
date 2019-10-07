import sys
from socket import *

def cat(a, b): 
    return a + b

def comp(a, b): 
    return 'Igual' if a == b else 'Diferente'

def subs(a, start, end):
    start = int(start)
    end = int(end)
    return a[start:end]

def contains(a, b):
    return 'sim' if a in b or b in a else 'nao'

def replace(a, b, c):
    return a.replace(b, c)

def default(*args):
    return '[ERROR] comando nao encontrado'

def parse(req):
    req = req.split()
    options = {
        'CONCATENAR': cat,
        'COMPARAR': comp,
        'SUBSTRING': subs,
        'CONTEM': contains,
        'SUBSTITUIR': replace
    }
    try:
        return options.get(req[0], default)(*req[1:])
    except:
        return '[ERROR]'

# print(parse('CONCATENAR com fome'))
# print(parse('COMPARAR aba aba'))
# print(parse('COMPARAR foo bar'))
# print(parse('SUBSTRING qwertyuiop 2 7'))
# print(parse('CONTEM foo bar'))
# print(parse('CONTEM abacaba a'))
# print(parse('SUBSTITUIR abacabadaba aba 16'))
# print(parse('NOPs'))

serverName = "localhost"
serverPort = int(sys.argv[1]) if len(sys.argv) > 1 else 9090

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverName,serverPort))

print ("The server is ready to receive")

while 1:
    sentence, addr = serverSocket.recvfrom(1024)
    sentence = sentence.decode('utf-8')
    
    serverSocket.sendto(parse(sentence).encode('utf-8'), addr)
    
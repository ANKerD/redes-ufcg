# -*- coding: utf-8 -*-
import socket
import sys
import os

# porta default 9090 (ou o que vier na linha de comando)
porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

staticfolder = 'static/'

# Leitura de dados
with socket.socket() as s:
  s.bind(('localhost', porta))
  s.listen()

  print('Aguardando conexões na porta %s...' % porta)
  while True:
    conexao, endereco = s.accept()
    with conexao:
      print('Conexão estabelecida de %s:%s' % endereco)
      req = conexao.recv(4096).decode('utf-8').splitlines()[0].split()
      method = 'GET'
      protocol = 'HTTP/1.1'
      headers = {
        'Host': socket.gethostbyname(socket.gethostname()),
      }
      body = ''
      if len(req) != 3:
        statusCode = 400
        statusMessage = 'Bad-Request'
      elif req[0].upper() != method:
        statusCode = 405
        statusMessage = 'Method-Not-Allowed'
      else:
        path = req[1]
        filepath = os.path.join(staticfolder, path[1:])
        if os.path.exists(filepath) and os.path.isfile(filepath):
          statusCode = 200
          statusMessage = 'OK'
          with open(filepath) as f:
            body = f.read()
        else:
          statusCode = 404
          statusMessage = 'Not-Found'
      firstLine = ' '.join([protocol, str(statusCode), statusMessage])
  
      ret = [firstLine]
      
      for key, value in headers.items():
        ret.append(key + ':' + value)

      ret.append('\n'+body)

      conexao.sendall('\n'.join(ret).encode('utf-8')) 
      

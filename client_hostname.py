import socket
import json

ip = '0.0.0.0'
porta = 8000
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))
arquivo_json = open('configuracoes.json', 'r')
dados_json = json.load(arquivo_json)
print(type(dados_json))
print(type(json.dumps(dados_json)))
print(dados_json['configuracoes'])
cliente.send(json.dumps(dados_json))
s = cliente.recv(1023)
print(s)

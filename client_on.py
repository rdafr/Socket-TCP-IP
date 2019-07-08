import socket
import json

ip = '192.168.0.125'
porta = 8000
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip, porta))
arquivo_json = open('configuracoes.json', 'rb')
#arquivo_json = open('configuracoes.json', 'r')
#dados_json = json.load(arquivo_json)
dados_json = arquivo_json.read()
print(type(dados_json))
"""print(type(dados_json))
print(type(json.dumps(dados_json)))
print(dados_json['configuracoes'])"""
#cliente.send(json.dumps(dados_json))
cliente.send(dados_json)
s = cliente.recv(1023)
print s

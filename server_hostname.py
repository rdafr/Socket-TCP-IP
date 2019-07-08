import socket
import json

ip = '0.0.0.0'
porta = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, porta))
server.listen(5)

while True:
	print("Esperando conexao: ")
	conexao, endereco = server.accept()
	print ('[*] Servidor conectado por', endereco)
	while True:
	        data2 = conexao.recv(1023)
		if not data2: break
       		conexao.send(data2)
        	print data2
        	with open('configuracoes_medidor.json','w') as outfile:
            		json.dump(json.loads(data2), outfile)
	conexao.close


            		
	

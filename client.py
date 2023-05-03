
# Guilherme Pereira Germano
# 507902

import socket
import random
import time

SERVER_ADDRESS = ('localhost', 5000)
MESSAGE_INTERVAL = 10 


# conectando com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)


while True:
    # sorteando um numero
    num = str(random.randint(1, 10**30))


    # enviando pro servidor
    client_socket.send(num.encode())


    # recebendo resposta do servidor
    response = client_socket.recv(1024).decode()
    print(response + "FIM")


    # pausa de 10 segundos
    time.sleep(MESSAGE_INTERVAL)


# Fim da conexao
client_socket.close()


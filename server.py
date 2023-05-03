import socket

SERVER_ADDRESS = ('localhost', 5000)
MAX_SIZE = 30

# Conectando com o cliente
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(1)

print("Servidor aguardando conexão...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Conexão estabelecida com", client_address)

    # recebendo numero do cliente
    num = client_socket.recv(1024).decode()
    print("Número recebido:", num)

    # verificando tamanho do numero
    if len(num) > MAX_SIZE:
        # enviando str do mesmo tamanho
        response = "A" * len(num)
        client_socket.send(response.encode())
    else:
        # verificando se é par ou impar
        if int(num) % 2 == 0:
            response = "PAR"
        else:
            response = "ÍMPAR"
        # enviando a resposta pro cliente
        client_socket.send(response.encode())

    # fechando conexão 
    client_socket.close()

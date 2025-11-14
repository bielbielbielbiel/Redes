# Importa o módulo socket 
from socket import * 
import sys  # Necessário para encerrar o programa 

# Cria o socket TCP (orientado à conexão) 
serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepara o socket do servidor 
#Fill in start 
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end 

while True: 
    # Estabelece a conexão 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()  #Fill in start     #Fill in end 

    try: 
        # Recebe a mensagem do cliente (requisição HTTP) 
        message = connectionSocket.recv(1024).decode()  #Fill in start     #Fill in end 

        filename = message.split()[1]   
        f = open(filename[1:]) 
        outputdata = f.read()  #Fill in start     #Fill in end 

        # Envia a linha de status do cabeçalho HTTP 
        #Fill in start 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end 

        # Envia o conteúdo do arquivo ao cliente 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 

        # Fecha a conexão com o cliente 
        connectionSocket.close() 

    except IOError: 
        # Envia mensagem de erro 404 se o arquivo não for encontrado 
        #Fill in start 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        #Fill in end 

        # Fecha o socket do cliente 
        #Fill in start 
        connectionSocket.close()
        #Fill in end 

    serverSocket.close() 
    sys.exit()  # Encerra o programa 

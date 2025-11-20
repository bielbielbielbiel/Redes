# http://127.0.0.1:6789/HelloWorld.html
# http://127.0.0.1:6789/nada.html


# Importa o módulo socket 
from socket import * 
import sys  # Necessário para encerrar o programa 

# Cria o socket TCP (orientado à conexão) 
serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepara o socket do servidor 

serverPort = 6789 # define o endereço IP e a porta do servidor 
serverSocket.bind(('', serverPort)) # '' = aceita conexões de qualquer IP
serverSocket.listen(1) # fica aguardando a conexão (Apenas uma)


while True: 
    # Estabelece a conexão 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() # cria uma nova conexão e armazena o endereço do cliente

    try: 
        # Recebe a mensagem do cliente (requisição HTTP) 
        message = connectionSocket.recv(1024).decode() # recebe até 1024 bytes / decode transforma em texto

        filename = message.split()[1]   # separa a requisição em partes e pega o segundo item(?HelloWrold)
        
        f = open(filename[1:]) # abre o arquivo no computador
        outputdata = f.read() # lê o HTML 

        # envia a linha de status do cabeçalho HTTP 

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) # Diz ao navegador qua a requisição foi bem sucedida / r,n separa o conteúdo

        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 

        # Fecha a conexão com o cliente 
        connectionSocket.close() 

    except IOError: 
        # Envia mensagem de erro 404 se o arquivo não for encontrado 
        # Página HTML dizendo que o arquivo não existe
    
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        # Fecha o socket do cliente 

        connectionSocket.close()

    serverSocket.close() 
    sys.exit()  # Encerra o programa 

import socket

LOCAL_HOST = "localhost"
SERVER_PORT = 7000
BUFFER_SIZE = 65500


def server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((LOCAL_HOST, SERVER_PORT))
    while True:
        clientMessage, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
        userInput = clientMessage.decode()
        print(f"Talking to the Client at the Address:{clientAddress}")
        print(f"Client Message:{userInput}")
        message = f"Hang in there client, I will get the IP Address of the \"{userInput}\""
        message = message.encode()
        serverSocket.sendto(message, clientAddress)
        for i in range(int(userInput)):
            number, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
            print(number.decode())


server()

import socket

LOCAL_HOST = "localhost"
SERVER_PORT = 7000
BUFFER_SIZE = 65500


def client(message):
    originalClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    originalClientMessage = message.encode()
    connectingAddress = (LOCAL_HOST, SERVER_PORT)
    originalClientSocket.sendto(originalClientMessage, connectingAddress)
    serverMessage, serverAddress = originalClientSocket.recvfrom(BUFFER_SIZE)
    serverMessage = serverMessage.decode()
    print(f"Talking to the Server at the Address: {serverAddress}")
    print(f"Message from {serverAddress}:")
    print(f"{serverMessage}")
    for i in range(int(message)):
        data = str(i).encode()
        originalClientSocket.sendto(data, connectingAddress)


client("5")

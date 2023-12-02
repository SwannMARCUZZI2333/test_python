
#client

import socket

client_socket = socket.socket()
client_socket.connect(('10.128.2.11', 10000))
print("Connexion établie...")

while True:
    message = input("vous (bye/arret pour quitter) : ")
    client_socket.send(message.encode())

    if message == "bye":
        print("Client arrêté.")
        client_socket.close()
        break
    elif message == "arret":
        print("server arrêté.")
        client_socket.close()
        break

    data = client_socket.recv(1024).decode()

    if data == "bye":
        print("Le serveur a terminé la connexion.")
        client_socket.close()
        break
    
    elif data == "arret":
        print("server arrêté.")
        client_socket.close()
        break

client_socket.close()
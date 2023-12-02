import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit
import socket
import threading

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.compteur = 0
        self.timer = QTimer(self)
        self.socket_server = None

        self.initUI()

    def initUI(self):
        self.label_compteur = QLabel('Compteur:', self)
        self.label_affichage = QLabel('0', self)
        self.edit_connect = QLineEdit(self)

        layout_principal = QVBoxLayout(self)
        layout_boutons = QGridLayout()

        bouton_start = QPushButton('Start', self)
        bouton_stop = QPushButton('Stop', self)
        bouton_reset = QPushButton('Reset', self)
        bouton_connect = QPushButton('Connect', self)
        bouton_quitter = QPushButton('Quitter', self)
        bouton_appliquer = QPushButton('Appliquer', self)

        layout_boutons.addWidget(bouton_start, 0, 0)
        layout_boutons.addWidget(bouton_stop, 0, 1)
        layout_boutons.addWidget(bouton_reset, 1, 0)
        layout_boutons.addWidget(bouton_connect, 1, 1)
        layout_boutons.addWidget(bouton_quitter, 2, 0)
        layout_boutons.addWidget(bouton_appliquer, 2, 1)

        bouton_start.clicked.connect(self.start_compteur)
        bouton_stop.clicked.connect(self.stop_compteur)
        bouton_reset.clicked.connect(self.reset_compteur)
        bouton_connect.clicked.connect(self.connect_to_edit)
        bouton_quitter.clicked.connect(self.quit_application)
        bouton_appliquer.clicked.connect(self.appliquer)

        layout_principal.addWidget(self.label_compteur)
        layout_principal.addWidget(self.label_affichage)
        layout_principal.addLayout(layout_boutons)
        layout_principal.addWidget(self.edit_connect)

        self.setLayout(layout_principal)

        self.timer.timeout.connect(self.incrementer_compteur)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Interface avec Qt6 et Python')
        self.show()

    def start_compteur(self):
        self.timer.start(1000)

    def stop_compteur(self):
        self.timer.stop()

    def reset_compteur(self):
        self.compteur = 0
        self.label_affichage.setText(str(self.compteur))

    def connect_to_edit(self):
        texte_edit = self.edit_connect.text()
        try:
            valeur = int(texte_edit)
            self.compteur = valeur
            self.label_affichage.setText(str(self.compteur))
        except ValueError:
            print("Mettre un nombre qui s'ajoute au compteur et connect")

    def appliquer(self):
        if self.socket_server:
            message = "Appliquer"
            self.socket_server.sendall(message.encode())
            print(f"Envoyé au serveur : {message}")
        else:
            print("Le socket n'est pas connecté.")

    def quit_application(self):
        self.close()

    def incrementer_compteur(self):
        self.compteur += 1
        self.label_affichage.setText(str(self.compteur))

def server_function():
    host = '127.0.0.1'  # localhost
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Serveur en attente de connexions sur {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Reçu du client : {message}")

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    # Lancer le serveur dans un thread séparé
    server_thread = threading.Thread(target=server_function)
    server_thread.start()

    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fenetre.socket_server.connect(('127.0.0.1', 5555))
    sys.exit(app.exec())

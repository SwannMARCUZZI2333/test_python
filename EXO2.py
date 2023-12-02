


import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.compteur = 0
        self.timer = QTimer(self)

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

        layout_boutons.addWidget(bouton_start, 0, 0)
        layout_boutons.addWidget(bouton_stop, 0, 1)
        layout_boutons.addWidget(bouton_reset, 1, 0)
        layout_boutons.addWidget(bouton_connect, 1, 1)
        layout_boutons.addWidget(bouton_quitter, 2, 0, 1, 2)

        bouton_start.clicked.connect(self.start_compteur)
        bouton_stop.clicked.connect(self.stop_compteur)
        bouton_reset.clicked.connect(self.reset_compteur)
        bouton_connect.clicked.connect(self.connect_to_edit)
        bouton_quitter.clicked.connect(self.quit_application)

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
            print("mettre un nombre qui ce ajoute au compteur et connect")

    def quit_application(self):
        self.close()

    def incrementer_compteur(self):
        self.compteur += 1
        self.label_affichage.setText(str(self.compteur))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    sys.exit(app.exec())

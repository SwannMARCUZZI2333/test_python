import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.compteur = 0
        self.label_compteur = QLabel('Compteur: 0', self)

        layout_principal = QVBoxLayout(self)

        bouton_start = QPushButton('Start', self)
        bouton_reset = QPushButton('Reset', self)
        bouton_quitter = QPushButton('Quitter', self)

        bouton_start.clicked.connect(self.start_compteur)
        bouton_reset.clicked.connect(self.reset_compteur)
        bouton_quitter.clicked.connect(self.close)

        layout_principal.addWidget(self.label_compteur)
        layout_principal.addWidget(bouton_start)
        layout_principal.addWidget(bouton_reset)
        layout_principal.addWidget(bouton_quitter)

        self.setLayout(layout_principal)

    def start_compteur(self):
        self.compteur += 1
        self.label_compteur.setText(f'Compteur: {self.compteur}')

    def reset_compteur(self):
        self.compteur = 0
        self.label_compteur.setText(f'Compteur: {self.compteur}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec())

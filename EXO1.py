import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        # Création juste en graphique pour exo 1 compteur
        self.compteur = 0
        self.label_compteur = QLabel('Compteur: 0', self)

        # Création de la mise en page principale
        layout_principal = QVBoxLayout(self)
        layout_boutons = QGridLayout()

        # Création juste en graphique pour exo 1 des cinq boutons
        bouton_start = QPushButton('Start', self)
        bouton_stop = QPushButton('Stop', self)
        bouton_reset = QPushButton('Reset', self)
        bouton_connect = QPushButton('Connect', self)
        bouton_quitter = QPushButton('Quitter', self)

        # Ajouter les boutons à la mise en page
        layout_boutons.addWidget(bouton_start, 0, 0)
        layout_boutons.addWidget(bouton_stop, 0, 1)
        layout_boutons.addWidget(bouton_reset, 1, 0)
        layout_boutons.addWidget(bouton_connect, 1, 1)
        layout_boutons.addWidget(bouton_quitter, 2, 0, 1, 2)

        # Connecter les signaux des boutons à des emplacements bidon (qui ne font rien)
        bouton_start.clicked.connect(self.bouton_appuye)
        bouton_stop.clicked.connect(self.bouton_appuye)
        bouton_reset.clicked.connect(self.bouton_reset)
        bouton_connect.clicked.connect(self.bouton_appuye)
        bouton_quitter.clicked.connect(self.close)

        # Ajouter le compteur à la mise en page
        layout_principal.addWidget(self.label_compteur)
        layout_principal.addLayout(layout_boutons)

        # Définir la mise en page principale du widget
        self.setLayout(layout_principal)

    def bouton_appuye(self):
        print(" bouton a été appuyé (mais il ne fait rien c'est normal car juste pour exo1 )")

    def bouton_reset(self):
        self.compteur = 0
        self.label_compteur.setText(f'Compteur: {self.compteur}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec())

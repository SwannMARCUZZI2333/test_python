
## programme faut, pas fini
import sys
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit

class WorkerThread(QThread):
    update_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stopped = False

    def run(self):
        compteur = 0
        while not self.stopped:
            compteur += 1
            self.update_signal.emit(compteur)
            self.msleep(1000)

    def stop(self):
        self.stopped = True
        self.wait()

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.compteur = 0
        self.timer = QTimer(self)
        self.worker_thread = WorkerThread()

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

        bouton_start.clicked.connect(self.start_compteur_threaded)
        bouton_stop.clicked.connect(self.stop_compteur_threaded)
        bouton_reset.clicked.connect(self.reset_compteur)
        bouton_connect.clicked.connect(self.connect_to_edit)
        bouton_quitter.clicked.connect(self.quit_application)

        layout_principal.addWidget(self.label_compteur)
        layout_principal.addWidget(self.label_affichage)
        layout_principal.addLayout(layout_boutons)
        layout_principal.addWidget(self.edit_connect)

        self.setLayout(layout_principal)

        self.worker_thread.update_signal.connect(self.afficher_compteur)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Interface avec Qt6 et Python')
        self.show()

    def start_compteur_threaded(self):
        self.worker_thread.start()

    def stop_compteur_threaded(self):
        self.worker_thread.stop()

    def reset_compteur(self):
        self.compteur = 0
        self.label_affichage.setText(f'Compteur: {self.compteur}')

    def connect_to_edit(self):
        texte_edit = self.edit_connect.text()
        try:
            valeur = int(texte_edit)
            self.compteur = valeur
            self.label_affichage.setText(f'Compteur: {self.compteur}')
        except ValueError:
            print("mettre un nombre qui ce ajoute au compteur et connect")

    def quit_application(self):
        self.worker_thread.stop()
        self.close()

    def afficher_compteur(self, compteur):
        self.label_affichage.setText(f'Compteur: {compteur}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    sys.exit(app.exec())

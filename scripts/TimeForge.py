import sys
from PyQt5 import QtWidgets
import run

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = run.DlgMain()  # Tworzenie instancji DlgMain z pliku run.py
    ui.show()
    sys.exit(app.exec_())

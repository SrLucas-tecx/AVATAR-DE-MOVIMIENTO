import sys
from PyQt5.QtWidgets import QApplication
from interface import Interface   # importamos la clase Interface desde interface.py

def main():
    app = QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

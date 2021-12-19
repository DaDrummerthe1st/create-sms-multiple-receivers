import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

class RenderPhonenumberGUI:
    def __init__(self):
        # instantiate QApplication using an empty list since no command line arguments will be accepted,
        # else use app = QApplication([sys.argv])
        self.app = QApplication([])

        # instantiate applications GUI
        self.window = QWidget()
        self.window.setWindowTitle('PyQt5 App')
        self.window.setGeometry(100, 100, 280, 80)
        self.window.move(60, 15)
        self.hello_msg = QLabel('<h1>Hello World!</h1>', parent=self.window)
        self.hello_msg.move(60, 15)


first_window = RenderPhonenumberGUI()
first_window.window.show()
sys.exit(first_window.app.exec_())

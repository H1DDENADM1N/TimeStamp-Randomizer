import sys
from PySide6.QtWidgets import QApplication, QWidget
from .resources.Ui_timestamp_randomizer import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

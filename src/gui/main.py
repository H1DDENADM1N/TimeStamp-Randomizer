import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from .resources.Ui_timestamp_randomizer import Ui_Form
from pathlib import Path


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ico_path = Path(__file__).parent / "resources/icon.ico"
        self.setWindowIcon(QIcon(str(ico_path)))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

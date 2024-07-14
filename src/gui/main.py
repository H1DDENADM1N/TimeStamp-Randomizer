import sys
from pathlib import Path

from loguru import logger
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget

from .resources.Ui_timestamp_randomizer import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ico_path = Path(__file__).parent / "resources/icon.ico"
        self.setWindowIcon(QIcon(str(ico_path)))
        self.setWindowOpacity(0.9)
        self.initUi()
        logger.info("Timestamp Randomizer GUI started")

    def initUi(self):
        pass


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

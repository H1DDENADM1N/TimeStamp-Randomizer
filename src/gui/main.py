import sys
from datetime import datetime
from pathlib import Path

from loguru import logger
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget

from ..timestamp_randomizer.config import RandomizeConfig
from ..timestamp_randomizer.folder_timestamp_manager import FolderTimestampManager
from .resources.Ui_timestamp_randomizer import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ico_path = Path(__file__).parent / "resources/icon.ico"
        self.setWindowIcon(QIcon(str(ico_path)))
        self.setWindowOpacity(0.9)

        self.selected_path: Path = None
        self.init_start_date()
        self.init_end_date()

        self.initUi()
        logger.info("Timestamp Randomizer GUI started")

    def initUi(self):
        self.pushButton_select_folder.clicked.connect(self.select_folder)
        self.pushButton_run.clicked.connect(self.run_randomizer)
        self.dateTimeEdit_start_date.dateTimeChanged.connect(self.update_start_date)
        self.dateTimeEdit_end_date.dateTimeChanged.connect(self.update_end_date)
        self.checkBox_same_caw.stateChanged.connect(self.on_same_caw_changed)
        self.checkBox_more_realistic.stateChanged.connect(
            self.on_more_realistic_changed
        )

    def on_same_caw_changed(self):
        if self.checkBox_same_caw.isChecked():
            # 创建时间 == 最后访问时间 == 最后修改时间
            RandomizeConfig.SAME_CAW = True
        else:
            RandomizeConfig.SAME_CAW = False

    def on_more_realistic_changed(self):
        if self.checkBox_more_realistic.isChecked():
            # 创建时间 <= 最后修改时间 <= 最后访问时间 <= 当前时间
            RandomizeConfig.MORE_REALISTIC = True
            if self.dateTimeEdit_end_date.dateTime().toPython() > datetime.now():
                self.dateTimeEdit_end_date.setDateTime(datetime.now())
        else:
            RandomizeConfig.MORE_REALISTIC = False
            self.init_end_date()

    def init_start_date(self):
        self.start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0)
        self.dateTimeEdit_start_date.setDateTime(self.start_date)

    def init_end_date(self):
        if RandomizeConfig.MORE_REALISTIC:
            self.end_date: datetime = datetime.now()
        else:
            self.end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59)
        self.dateTimeEdit_end_date.setDateTime(self.end_date)

    def update_start_date(self):
        if (
            RandomizeConfig.MORE_REALISTIC
            and self.dateTimeEdit_start_date.dateTime().toPython()
            > self.dateTimeEdit_end_date.dateTime().toPython()
        ):
            self.dateTimeEdit_start_date.setDateTime(
                self.dateTimeEdit_end_date.dateTime().toPython()
            )
        else:
            self.start_date: datetime = (
                self.dateTimeEdit_start_date.dateTime().toPython()
            )
        logger.info(f"Updated start date: {self.start_date}")

    def update_end_date(self):
        if (
            RandomizeConfig.MORE_REALISTIC
            and self.dateTimeEdit_end_date.dateTime().toPython() > datetime.now()
        ):
            self.dateTimeEdit_end_date.setDateTime(datetime.now())
        else:
            self.end_date: datetime = self.dateTimeEdit_end_date.dateTime().toPython()
        logger.info(f"Updated end date: {self.end_date}")

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select a Folder", "")
        if folder_path:
            self.selected_path = Path(folder_path)
            logger.info(f"Selected folder: {self.selected_path}")
        else:
            self.selected_path = None
            logger.info("Cancelled Select a Folder")

    def run_randomizer(self):
        if not self.selected_path:
            logger.info("Please select a folder first.")
            return

        logger.info(
            f"Starting randomizer on folder: {self.selected_path}\nStart date: {self.start_date}\nEnd date: {self.end_date}"
        )

        manager = FolderTimestampManager(self.selected_path)
        manager.log_folder_timestamps()
        manager.randomize_folder_timestamps(self.start_date, self.end_date)

        self.textEdit_info.append_log("\x1b[94m\x1b[92mRandomization completed.\x1b[0m")


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

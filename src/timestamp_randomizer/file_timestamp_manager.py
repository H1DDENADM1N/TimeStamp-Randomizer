import sqlite3
from datetime import datetime
from pathlib import Path

from loguru import logger
from pywintypes import Time
from utils.create_table import create_table
from utils.get_randomized_timestamps import get_randomized_timestamps
from win32con import (
    FILE_FLAG_BACKUP_SEMANTICS,
    FILE_SHARE_DELETE,
    FILE_SHARE_READ,
    FILE_SHARE_WRITE,
    GENERIC_READ,
    GENERIC_WRITE,
    OPEN_EXISTING,
)
from win32file import (
    CloseHandle,
    CreateFile,
    SetFileTime,
)


class FileTimestampManager:
    db_path = Path(r"C:\Users\user0\Documents\TimeStamp-Randomizer\tests\test.db")

    def __init__(self, file_path: Path):
        self.file_path = file_path
        if not self.db_path.exists():
            create_table(self.db_path)

    def is_file_exists(self) -> bool:
        """
        判断文件是否存在。

        :return: 文件是否存在
        """
        if not self.file_path.exists():
            logger.error(f"The file {self.file_path} does not exist.")
            return False
        if not self.file_path.is_file():
            logger.error(f"The path {self.file_path} is a directory, not a file.")
            return False

        return True

    def log_file_timestamps(self):
        """
        记录文件的创建时间、最后修改时间和最后访问时间。
        """
        # 检查文件是否存在
        if not self.is_file_exists():
            return

        creation_time = datetime.fromtimestamp(
            self.file_path.stat().st_ctime
        ).isoformat()
        last_access_time = datetime.fromtimestamp(
            self.file_path.stat().st_atime
        ).isoformat()
        last_write_time = datetime.fromtimestamp(
            self.file_path.stat().st_mtime
        ).isoformat()

        logger.info(
            f"\n\t{self.file_path}\n\tcreation_time:\t\t{creation_time}\n\tlast_access_time:\t{last_access_time}\n\tlast_write_time:\t{last_write_time}"
        )

        # 记录文件时间戳到数据库
        conn = sqlite3.connect(str(self.db_path))
        c = conn.cursor()
        c.execute(
            """INSERT INTO file_timestamps (id, log_time, file_path, creation_time, last_access_time, last_write_time) VALUES (?,?,?,?,?,?)""",
            (
                None,
                datetime.now().isoformat(),
                str(self.file_path),
                creation_time,
                last_access_time,
                last_write_time,
            ),
        )
        conn.commit()
        conn.close()

    def set_file_timestamps(
        self,
        creation_time: datetime = datetime.now(),
        last_access_time: datetime = datetime.now(),
        last_write_time: datetime = datetime.now(),
    ):
        """
        设置文件的创建时间、最后修改时间和最后访问时间。

        :param creation_time: 创建时间，默认为当前时间
        :param last_access_time: 最后访问时间，默认为当前时间
        :param last_write_time: 最后修改时间，默认为当前时间
        """
        # 检查文件是否存在
        if not self.is_file_exists():
            return

        # 获取文件句柄
        file_handle = CreateFile(
            str(self.file_path),
            GENERIC_READ | GENERIC_WRITE,
            FILE_SHARE_WRITE | FILE_SHARE_READ | FILE_SHARE_DELETE,
            None,
            OPEN_EXISTING,
            FILE_FLAG_BACKUP_SEMANTICS,
            None,
        )

        try:
            # 设置文件时间戳
            logger.info(f"Setting file timestamps for {self.file_path}")
            SetFileTime(
                file_handle.handle,
                Time(creation_time.timetuple()),
                Time(last_access_time.timetuple()),
                Time(last_write_time.timetuple()),
            )
        except Exception as e:
            logger.error(f"Failed to set file timestamps: {e}")
        finally:
            # 确保文件句柄被关闭
            CloseHandle(file_handle.handle)

    def randomize_file_timestamps(
        self,
        start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0),
        end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59),
    ):
        """
        随机化文件的创建时间、最后修改时间和最后访问时间。

        :param start_date: 开始时间，默认为当前年份的1月1日
        :param end_date: 结束时间，默认为当前年份的12月31日
        """
        c, a, w = get_randomized_timestamps(start_date, end_date)
        logger.info(
            f"\n\tRandomizing file timestamps for {self.file_path}\n\trandomized_creation_time:\t{c}\n\trandomized_last_access_time:\t{a}\n\trandomized_last_write_time:\t{w}"
        )
        self.set_file_timestamps(creation_time=c, last_access_time=a, last_write_time=w)


if __name__ == "__main__":
    FileTimestampManager.db_path = Path(
        r"C:\Users\user0\Documents\TimeStamp-Randomizer\tests\test.db"
    )

    file_path = Path(
        r"C:\Users\user0\Documents\TimeStamp-Randomizer\tests\test_folder\test.txt"
    )
    manager = FileTimestampManager(file_path)

    manager.log_file_timestamps()  # 记录文件原始时间戳

    # 随机化文件时间戳
    # manager.randomize_file_timestamps()

    # 指定时间范围随机化
    manager.randomize_file_timestamps(
        datetime(2012, 1, 1, 0, 0, 0), datetime(2077, 12, 31, 23, 59, 59)
    )

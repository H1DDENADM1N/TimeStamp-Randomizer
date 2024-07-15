import sqlite3
from datetime import datetime
from pathlib import Path
from turtle import st

from loguru import logger
from pywintypes import Time
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

from .file_timestamp_manager import FileTimestampManager
from .utils.create_table import create_table
from .utils.get_randomized_timestamps import get_randomized_timestamps


class FolderTimestampManager:
    db_path = Path(r"C:\Users\user0\Documents\TimeStamp-Randomizer\tests\test.db")

    def __init__(self, folder_path: Path):
        self.folder_path = folder_path
        if not self.db_path.exists():
            create_table(self.db_path)

    def is_folder_exists(self) -> bool:
        """
        判断文件夹是否存在。

        :return: 文件夹是否存在。
        """
        if not self.folder_path.exists():
            logger.error(f"Folder {self.folder_path} does not exist.")
            return False
        if not self.folder_path.is_dir():
            logger.error(f"Path {self.folder_path} is not a directory.")
            return False

        return True

    def log_folder_timestamps(self) -> None:
        """
        记录文件夹的创建时间戳。
        """
        # 检查文件夹是否存在
        if not self.is_folder_exists():
            return

        creation_time: str = datetime.fromtimestamp(
            self.folder_path.stat().st_ctime
        ).isoformat()
        last_access_time: str = datetime.fromtimestamp(
            self.folder_path.stat().st_atime
        ).isoformat()
        last_write_time: str = datetime.fromtimestamp(
            self.folder_path.stat().st_mtime
        ).isoformat()

        logger.info(
            f"\n\t{self.folder_path}\\\n\tcreation_time:\t\t{creation_time}\n\tlast_access_time:\t{last_access_time}\n\tlast_write_time:\t{last_write_time}"
        )

        # 记录文件夹时间戳到数据库
        conn = sqlite3.connect(str(self.db_path))
        c = conn.cursor()
        c.execute(
            """INSERT INTO folder_timestamps (id, log_time, folder_path, creation_time, last_access_time, last_write_time) VALUES (?, ?, ?, ?, ?, ?)""",
            (
                None,
                datetime.now().isoformat(),
                str(self.folder_path),
                creation_time,
                last_access_time,
                last_write_time,
            ),
        )
        conn.commit()
        conn.close()

    def set_folder_timestamps(
        self,
        creation_time: datetime = datetime.now(),
        last_access_time: datetime = datetime.now(),
        last_write_time: datetime = datetime.now(),
        /,
        start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0),
        end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59),
    ) -> None:
        """
        设置文件夹的时间戳。
        先递归遍历文件夹，然后设置每个子文件的创建时间、最后访问时间、最后修改时间。

        :param creation_time: 文件夹的创建时间。
        :param last_access_time: 文件夹的最后访问时间。
        :param last_write_time: 文件夹的最后修改时间。

        :param start_date: 开始时间，默认为当前年份的1月1日，用于递归遍历随机化子文件时间戳。
        :param end_date: 结束时间，默认为当前年份的12月31日，用于递归遍历随机化子文件时间戳。
        """
        # 检查文件夹是否存在
        if not self.is_folder_exists():
            return

        # 递归遍历文件夹
        for child in self.folder_path.iterdir():
            if child.is_dir():
                child_manager = FolderTimestampManager(child)
                child_manager.log_folder_timestamps()
                child_manager.set_folder_timestamps(
                    creation_time,
                    last_access_time,
                    last_write_time,
                    start_date=start_date,
                    end_date=end_date,
                )
            elif child.is_file():
                child_manager = FileTimestampManager(child)
                child_manager.log_file_timestamps()
                child_manager.randomize_file_timestamps(start_date, end_date)

        # 获取文件夹句柄
        folder_handle = CreateFile(
            str(self.folder_path),
            GENERIC_READ | GENERIC_WRITE,
            FILE_SHARE_WRITE | FILE_SHARE_READ | FILE_SHARE_DELETE,
            None,
            OPEN_EXISTING,
            FILE_FLAG_BACKUP_SEMANTICS,
            None,
        )

        try:
            # 设置文件夹的时间戳
            logger.info(f"Setting folder timestamps for {self.folder_path}")
            SetFileTime(
                folder_handle,
                Time(creation_time.timetuple()),
                Time(last_access_time.timetuple()),
                Time(last_write_time.timetuple()),
            )
        except Exception as e:
            logger.error(f"Failed to set folder timestamps for {self.folder_path}: {e}")
        finally:
            # 确保文件句柄被关闭
            CloseHandle(folder_handle)
            logger.debug(f"Exiting set_folder_timestamps for {self.folder_path}")

    def randomize_folder_timestamps(
        self,
        start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0),
        end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59),
    ):
        """
        随机化文件夹的创建时间、最后修改时间、最后访问时间。

        :param start_date: 开始时间，默认为当前年份的1月1日
        :param end_date: 结束时间，默认为当前年份的12月31日
        """
        c, a, w = get_randomized_timestamps(start_date, end_date)
        logger.info(
            f"\n\tRandomizing folder timestamps for {self.folder_path}\n\trandomized_creation_time:\t{c}\n\trandomized_last_access_time:\t{a}\n\trandomized_last_write_time:\t{w}"
        )
        self.set_folder_timestamps(
            c,
            a,
            w,
            start_date=start_date,
            end_date=end_date,
        )

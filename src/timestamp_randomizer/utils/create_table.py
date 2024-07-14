import sqlite3
from pathlib import Path


def create_table(db_path: Path):
    """
    创建数据库表用于记录文件时间戳。
    """
    conn = sqlite3.connect(str(db_path))
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS file_timestamps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            file_path TEXT,
            creation_time TIMESTAMP,
            last_access_time TIMESTAMP,
            last_write_time TIMESTAMP
        )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS folder_timestamps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            folder_path TEXT,
            creation_time TIMESTAMP,
            last_access_time TIMESTAMP,
            last_write_time TIMESTAMP
        )"""
    )
    conn.commit()
    conn.close()

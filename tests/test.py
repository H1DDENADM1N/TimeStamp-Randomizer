import sys
from datetime import datetime
from pathlib import Path

current_working_dir = Path().cwd()
src_path = current_working_dir / "src"
sys.path.append(str(src_path))

from timestamp_randomizer.file_timestamp_manager import FileTimestampManager
from timestamp_randomizer.folder_timestamp_manager import FolderTimestampManager


def test_file_timestamp_manager():
    test_txt_path = Path(__file__).parent / "test_folder" / "test.txt"
    manager = FileTimestampManager(test_txt_path)
    manager.log_file_timestamps()
    # manager.set_file_timestamp()
    # manager.randomize_file_timestamp()
    manager.randomize_file_timestamps(
        datetime(2012, 1, 1, 0, 0, 0), datetime(2077, 12, 31, 23, 59, 59)
    )


def test_folder_timestamp_manager():
    test_folder_path = Path(__file__).parent / "test_folder"
    manager = FolderTimestampManager(test_folder_path)
    manager.log_folder_timestamps()
    # manager.set_folder_timestamps()
    manager.randomize_folder_timestamps()


if __name__ == "__main__":
    test_file_timestamp_manager()
    print("\n\n\n\n")
    test_folder_timestamp_manager()

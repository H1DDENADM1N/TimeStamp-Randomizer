import sys
from datetime import datetime
from pathlib import Path

current_working_dir = Path().cwd()
src_path = current_working_dir / "src"
sys.path.append(str(src_path))

from timestamp_randomizer.file_timestamp_manager import FileTimestampManager
from timestamp_randomizer.folder_timestamp_manager import FolderTimestampManager

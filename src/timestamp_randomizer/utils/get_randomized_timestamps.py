from datetime import datetime

from loguru import logger

from ..config import RandomizeConfig
from .get_randomized_date import get_randomized_date


def get_randomized_timestamps(
    start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0),
    end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59),
) -> tuple[datetime, datetime, datetime]:
    """
    获取随机化的时间戳

    :param start_date: 开始时间
    :param end_date: 结束时间
    :return: 随机化的时间戳
    """
    # 确保开始时间小于结束时间
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    if RandomizeConfig.SAME_CAW:
        # 创建时间 == 最后访问时间 == 最后修改时间
        logger.debug("Randomizing file timestamps with SAME_CAW config")
        creation_time: datetime = get_randomized_date(start_date, end_date)
        last_access_time: datetime = creation_time
        last_write_time: datetime = creation_time
    elif RandomizeConfig.MORE_REALISTIC:
        # 创建时间 <= 最后修改时间 <= 最后访问时间 <= 当前时间
        logger.debug("Randomizing file timestamps with MORE_REALISTIC config")

        now = datetime.now()
        if start_date <= end_date <= now:
            pass
        if end_date > now:
            end_date = now
        if start_date > now:
            start_date = now

        last_access_time: datetime = get_randomized_date(start_date, end_date)
        last_write_time: datetime = get_randomized_date(start_date, last_access_time)
        creation_time: datetime = get_randomized_date(start_date, last_write_time)
    else:
        # 随机化所有时间戳
        creation_time: datetime = get_randomized_date(start_date, end_date)
        last_access_time: datetime = get_randomized_date(start_date, end_date)
        last_write_time: datetime = get_randomized_date(start_date, end_date)

    return creation_time, last_access_time, last_write_time

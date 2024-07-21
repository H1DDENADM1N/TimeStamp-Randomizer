import random
from datetime import datetime, timedelta

from ..config import RandomizeConfig


def get_randomized_date(
    start_date: datetime = datetime(datetime.now().year, 1, 1, 0, 0, 0),
    end_date: datetime = datetime(datetime.now().year, 12, 31, 23, 59, 59),
) -> datetime:
    """
    获取随机化的日期。

    :param start_date: 开始时间，默认为当前年份的1月1日
    :param end_date: 结束时间，默认为当前年份的12月31日
    :return: 随机化的日期
    """
    seconds_between_date: int = abs(int((end_date - start_date).total_seconds()))
    random_seconds: int = random.randrange(seconds_between_date)
    random_date: datetime = start_date + timedelta(seconds=random_seconds)
    if RandomizeConfig.NINE_TO_FIVE:
        # 随机化的时间范围为 9:00 ~ 17:00
        if random_date.hour < 9:
            random_hour: int = random.randrange(max(9, start_date.hour), 17)
        elif random_date.hour > 17:
            random_hour: int = random.randrange(9, min(17, end_date.hour))
        else:
            random_hour: int = random_date.hour
        random_date: datetime = random_date.replace(hour=random_hour)
    # logger.debug(f"Random date: {random_date}")
    return random_date

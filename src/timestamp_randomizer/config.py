from dataclasses import dataclass


@dataclass()
class RandomizeConfig:
    SAME_CAW: bool = False  # 创建时间 == 最后访问时间 == 最后修改时间
    MORE_REALISTIC: bool = True  # 创建时间 <= 最后修改时间 <= 最后访问时间 <= 当前时间
    NINE_TO_FIVE: bool = True  # 随机化的时间范围为 9:00 ~ 17:00

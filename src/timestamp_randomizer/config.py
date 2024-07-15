from dataclasses import dataclass


@dataclass()
class RandomizeConfig:
    SAME_CAW: bool = False  # 创建时间 == 最后访问时间 == 最后修改时间
    MORE_REALISTIC: bool = True  # 创建时间 <= 最后修改时间 <= 最后访问时间 <= 当前时间

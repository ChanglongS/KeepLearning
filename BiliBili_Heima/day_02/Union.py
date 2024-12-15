# Union
from typing import Union

my_list: list[Union[str, int]] = [1, 2, 3, "str"]


def func(data: Union[str, int]) -> Union[str, int]:
    pass


func("22")

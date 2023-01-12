import math
from tvm_base import TVMBase


class FV(TVMBase):
    def __init__(self, start_value, rate, periods):
        self._start_value = start_value
        self._rate = rate
        self._periods = periods

    def calculate(self):
        self._end_value = self._start_value * math.pow(1 + self._rate, self._periods)


if __name__ == "__main__":
    fv = FV(100, 0.1, 2)
    breakpoint
    fv.calculate()
    print(fv.get_end_value())

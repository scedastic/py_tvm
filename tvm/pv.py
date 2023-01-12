import math
from tvm_base import TVMBase


class PV(TVMBase):
    def __init__(self, end_value, rate, periods):
        self._end_value = end_value
        self._rate = rate
        self._periods = periods

    def calculate(self):
        self._start_value = self._end_value / math.pow(1 + self._rate, self._periods)


if __name__ == "__main__":
    pv = PV(100, 0.05, 2)
    breakpoint
    pv.calculate()
    print(pv.get_start_value())

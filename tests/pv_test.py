import pytest
import tvm

class PVTest:
    def simple_pv_test(self):
        pv = PV(110, 10, 1)
        assert pv.get_start_value() == 100

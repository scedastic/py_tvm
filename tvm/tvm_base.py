class TVMBase:
    '''
        Base class for simple TVM such as Present Value and Future Value
        There is an attempt to keep some sort of data encapsulation.
        Violate at your own risk.
    '''
    def __init__(self):
        self._start_value = 0.0
        self._rate = 0.0
        self._periods = 0
        self._end_value = 0.0

    ''' Property setters and getters '''

    def set_start_value(self, start_value):
        self._start_value = start_value
        self.calculate()
        
    def set_rate(self, rate):
        self._rate = rate
        self.calculate()
        
    def set_periods(self, periods):
        self._periods = periods
        self.calculate()
        
    def set_end_value(self, end_value):
        self._end_value = end_value
        self.calculate()

    def get_start_value(self):
        return self._start_value
        
    def get_rate(self):
        return self._rate
        
    def get_periods(self):
        return self._periods
        
    def get_end_value(self):
        return self._end_value
        
    def calculate(self):
        pass
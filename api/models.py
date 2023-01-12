import math
from pydantic import BaseModel, PositiveInt

class TVM(BaseModel):
    start_value: float = 0.0
    rate: float = 0.0
    periods: PositiveInt
    end_value: float = 0.0
    
    def calculate(self):
        """The value to be calculated will be the one that is set to 0(.0)"""
        if self.start_value == 0.0: # We are solving for PV
            denominator = math.pow(1 + self.rate, self.periods)
            if denominator != 0:
                self.start_value = self.end_value / denominator
        elif self.end_value == 0.0: # We are solving for FV
            self.end_value = self.start_value * math.pow(1 + self.rate, self.periods)
        elif self.periods == 0: # We are looking for how many terms are required to reach (exceed) our goal
            log_a_term = self.end_value/self.start_value 
            if log_a_term != 0:
                self.periods = math.ceil(math.log(log_a_term) / math.log(1 + rate))
        elif self.rate == 0.0:  # We are looking for the rate of return
            log_a_term = self.end_value/self.start_value 
            if log_a_term != 0:
                log_a = math.log(log_a_term)
                self.rate = math.exp(log_a / self.periods)
    
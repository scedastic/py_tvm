from fastapi import FastAPI
import math
from models import TVM

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello Wordl"}

@app.get('/pv')
async def pv(endValue: float, rate: float = 0.0, periods: int = 1):
    '''
    Based on the TVM formula for the Present value of a future payment.
    '''
    x = TVM(end_value = endValue, rate = rate, periods = periods)
    x.calculate()
    return x

@app.get('/fv')
async def fv(startValue: float, rate: float = 0.0, periods: int = 1):
    '''
    Based on the TVM formula for the future value of money.
    '''
    x = TVM(start_value = startValue, rate = rate, periods = periods)
    x.calculate()
    return x

@app.get('/rate')
async def rate(startValue: float, endValue: float, periods: int):
    x = TVM(start_value=startValue, end_value = endValue, periods = periods)
    x.calculate()

    
@app.get('/periods')
async def rate(startValue: float, endValue: float, rate: float):
    x = TVM(start_value=startValue, end_value = endValue, rate = rate)
    x.calculate()
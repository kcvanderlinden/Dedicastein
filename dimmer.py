from machine import Timer, Pin
from micropython import alloc_emergency_exception_buf
from math import acos, pi

# only tested with a lamp
class Dimmer:
    def __init__(self, pwm_pin, zc_pin, fpulse = 4000):
        alloc_emergency_exception_buf(100)
        self._cnt    = 0
        self._freq   = 140
        self._timer  = Timer()
        self.triacFiringPin = Pin(pwm_pin, Pin.OUT, value=0)
        self._fpulse = fpulse
        self._ppulse = 100.0 / fpulse + 0.11
        self.zeroCrossoverPin = Pin(zc_pin, Pin.IN, Pin.PULL_DOWN)
        self._val    = 1
        self.zeroCrossoverPin.irq(trigger=Pin.IRQ_RISING, handler=self.ZeroCrossover)

    def triacpulse(self, a):
        global dummy
        self.triacFiringPin.high()
        for x in range (50): pass
        self.triacFiringPin.low()
        
    def ZeroCrossover(self, arg):
        self.triacFiringPin.low()
        self._timer.init(freq=self._freq,mode=Timer.ONE_SHOT,callback=self.triacpulse)
    
    @property
    def value(self):
        return self._val
    
    
    @value.setter
    def value(self, p):
        p = p/100
        self._val = p
        p = min(1, max(0, p))
        p = acos(1 - p * 2) / pi
                
        if p < 0.15 :
            self._freq = 20
        elif p > 0.99:
            self._freq = 0
        else:
            self._freq = int(100 / (1 - p))
        print(f"value set as {self._freq}")
        self.zeroCrossoverPin.irq(trigger=Pin.IRQ_RISING, handler=self.ZeroCrossover)
        return self._val

'''dimmer = Dimmer(21, 20)        
while True:
    dimmer.value = int(input ( "enter number between 1 and 100: " ))'''



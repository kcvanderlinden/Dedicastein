from thermoster import read_temperature
from machine import Pin, PWM
from PID import PID
import asyncio
import time
from dedicamodules import handle_relay_by_buttons

# Constants
TARGET_TEMPERATURE = 80.0 # Desired temperature in Celsius
PWM_FREQUENCY = 50         # PWM frequency in Hz
MAX_DUTY_CYCLE = 65535     # Maximum duty cycle for Pico's PWM (16-bit resolution)

# Initialize the SSR pin and PWM
ssr_pin = Pin(22, Pin.OUT)  # Replace with your SSR GPIO pin number
pwm_ssr = PWM(ssr_pin)
pwm_ssr.freq(PWM_FREQUENCY)

pid = PID(600, .5, 5, setpoint=TARGET_TEMPERATURE)
pid.output_limits = (0, 65535)

# time
last_time = time.ticks_ms()

def get_temperature():
    return read_temperature()

while True:
    # Run the main event loop
    asyncio.run(handle_relay_by_buttons())
    current_time = time.ticks_ms()
    current_temp = get_temperature()
    power = pid(current_temp)
    duty_cycle = max(0, min(MAX_DUTY_CYCLE, int(power)))
    pwm_ssr.duty_u16(duty_cycle)
    if (current_time - last_time) / 1000 > 1: # log every second
        
        last_time = current_time
        print(f"Current Temperature: {current_temp:.2f}°C")
        print(power)

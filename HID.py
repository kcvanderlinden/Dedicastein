from machine import Pin
import time

# Define the GPIO pins on Raspberry Pi Pico that correspond to the wires
wire1 = Pin(0, Pin.OUT)  # Input with pull-up resistor for switch 1
wire2 = Pin(1, Pin.OUT)  # Input with pull-up resistor for switch 3
wire3 = Pin(2, Pin.OUT)
wire4 = Pin(3, Pin.OUT)
wire5 = Pin(4, Pin.OUT)
wire6 = Pin(5, Pin.OUT)

led1 = wire4
led2 = wire4
led3 = wire4
led4 = wire3

def set_led(led_pins, state):
    """Set the LED to on or off."""
    led_pins.value(state)
        
set_led(wire4, 0)
set_led(wire3, 0)
set_led(wire5, 1)

def read_switches():
    """Read the switches and return their states."""
    switch1_state = bool(wire2.value())  # Active low due to pull-up resistor
    switch2_state = bool(wire1.value())# Detects voltage drop with diode
    switch3_state = bool(not wire6.value())  # Detects voltage drop with diode
    
    return switch1_state, switch2_state, switch3_state

count = 0
# Main loop to check button presses and control LEDs
while True:
    
    # print(read_switches())
    if True in read_switches():
        count += 1
        print(read_switches(), count)
    # Check switch 1 state


    time.sleep(0.1)  # Small delay to avoid debouncing issues

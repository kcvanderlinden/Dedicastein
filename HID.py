from machine import Pin
import time

# Define the GPIO pins on Raspberry Pi Pico that correspond to the wires
wire1 = Pin(0, Pin.IN, Pin.PULL_UP) # Input with pull-up resistor for switch 1
wire2 = Pin(1, Pin.IN, Pin.PULL_UP)  # Input with pull-up resistor for switch 3
wire3 = Pin(2, Pin.OUT)
wire4 = Pin(3, Pin.OUT)
wire5 = Pin(4, Pin.OUT)
wire6 = Pin(5, Pin.IN, Pin.PULL_UP)

def read_switches():
    """Read the switches and return their states."""
    switch_small = bool(wire3.value())  # Detects voltage drop with diode
    switch_big = bool(wire4.value())
    
    return switch_small, switch_big

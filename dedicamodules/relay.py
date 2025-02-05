from machine import Pin
import asyncio

coffee_small = Pin(2, Pin.OUT) # Input with pull-up resistor for switch 1
wire2 = Pin(3, Pin.OUT)  # Input with pull-up resistor for switch 3
wire3 = Pin(4, Pin.OUT)
wire4 = Pin(5, Pin.OUT)
#wire5 = Pin(6, Pin.OUT)
wire6 = Pin(6, Pin.IN)
relay_pin = Pin(14, Pin.OUT)

pump_switch = Pin(10, Pin.OUT)

# Global flag to indicate interrupt occurred
interrupt_occurred = False

def toggle_coffee(pin):
    global interrupt_occurred
    interrupt_occurred = True

async def handle_interrupts():
    global interrupt_occurred
    while True:
        if interrupt_occurred:
            print("Interrupt occurred, toggling coffee pin")
            await toggle_pin(coffee_small)
            interrupt_occurred = False
        await asyncio.sleep_ms(10)  # Yield control to other tasks
        
async def toggle_pin(pin):
    print("pressed")
    pump_switch.value(1)
    await asyncio.sleep_ms(1000)
    #await asyncio.sleep_ms(100)
    pump_switch.value(0)
    
async def handle_relay_by_buttons():
    coffee_small.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle_coffee)
    
    task1 = asyncio.create_task(handle_interrupts())
    await asyncio.gather(task1)



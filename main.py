from thermoster import read_temperature
from time import sleep

while True:
    temperature = read_temperature()
    print(f"Temperature: {temperature:.2f} °C")
    sleep(1)
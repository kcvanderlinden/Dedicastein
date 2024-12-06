from machine import Pin, ADC
import math


# Set up the ADC pin for reading the sensor
adc = ADC(Pin(28))  # Assuming GP0 is connected to the NST sensor

def read_temperature():
    # Read the raw value from the ADC
    adc_value_average = 0
    number_of_measurements = 1000 # the reading of the ADC is noisy whereby the temprature fluctuates. Taking multiple measurements and making an average is a temporary solution.
    for i in range(number_of_measurements):
        adc_value_average += adc.read_u16()
    adc_value = adc_value_average / number_of_measurements
    
    # Convert the ADC value to voltage (assuming a reference of 3.3V)
    
    voltage = adc_value * (3.3 / 65535)  # 65535 is the maximum ADC value
    
    # Convert voltage to resistance using the voltage divider formula
    # Assume you have a resistor R1 in series with the sensor, and measure the voltage across it
    # Let's say R1 = 10k ohms for this example
    R1 = 10000
    
    R_sensor = (voltage * R1) / (3.3 - voltage)
    
    # Calculate temperature using the Steinhart-Hart equation or a simpler approximation
    # For simplicity, we'll use a linear approximation here:
    # This is a rough approximation and will need to be calibrated for your specific sensor
    B_constant = 3950  # I do not have the datasheet, but this constant seems to work
    T0 = 298.15  # 25°C in Kelvin
    R0 = 86500  # Should be the resistance at 25 °C, calibrated atm with a meat thermometer
    
    # Steinhart-Hart equation: ln(R/R0) = B * (1/T - 1/T0)
    temp_kelvin = B_constant / (B_constant * (1/T0) + math.log(R_sensor/R0))
    temp_celsius = temp_kelvin - 273.15
    
    return temp_celsius

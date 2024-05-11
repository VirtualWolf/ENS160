from machine import Pin, I2C
from ens160 import ENS160

i2c = I2C(0, sda=Pin(23), scl=Pin(22))

# Sensor can also be initialised with a specific I2C address and the current
# temperature and humidity values if you have them available:
#
#   sensor = ENS160(i2c=i2c, address=0x52, temperature=20, humidity=65)
sensor = ENS160(i2c=i2c)

# Returns a tuple of air quality index from 1 (very good) to 5 (very bad), eCO2
# in parts per million and total volatile organic compounds in parts per billion
(aqi, tvoc, eco2) = sensor.get_readings()

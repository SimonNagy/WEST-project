import bme280
import smbus2

# configuration of hardware ports
port = 1 # potentially can be 0 if the RPi is older
address = "0x76"
bus = smbus2.SMBus(port)

# loading calibration params and reading a single line of data
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

# compensated reading object returned form above; has the following params
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# string representation of the data
print(data)
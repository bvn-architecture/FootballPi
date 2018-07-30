from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor {} {} has temperature {}".format(sensor, sensor.id, sensor.get_temperature()))
    id = sensor.id

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, id)
temperature_in_celsius = sensor.get_temperature()
print(temperature_in_celsius)


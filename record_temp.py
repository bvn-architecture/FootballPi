from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))


sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "00000588806a")
temperature_in_celsius = sensor.get_temperature()

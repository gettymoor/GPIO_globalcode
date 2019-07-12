import pyowm

apikey = 'f13f347a55bfd4e43fb59503bca14177'
owm=pyowm.OWM('f13f347a55bfd4e43fb59503bca14177')
obs = owm.weather_at_place('hong kong,china')
obs = owm.weather_at_place('tokyo,japan')
w = obs.get_weather()
q = obs.get_weather()

#q = obs.get_weather()

print("in hong kong,china")
print("in tokyo,japan")
print("the reference time is", w.get_reference_time())
print("the cloud is", w.get_clouds())
print("the wind is", w.get_wind())
print("the humidityis", w.get_humidity())
print("the pressure is", w.get_pressure())
print("the temperature is", w.get_temperature(unit='celsius'))
print("the status is", w.get_status())
print(" ")
print(" ")
print(" ")


print("the reference time is", q.get_reference_time())
print("the cloud is", q.get_clouds())
print("the wind is", q.get_wind())
print("the humidityis", q.get_humidity())
print("the pressure is", q.get_pressure())
print("the temperature is", q.get_temperature(unit='celsius'))
print("the status is", q.get_status())


if( w.get_humidity()> q.get_humidity()):
    print("the humidity in tokyo is high")

else:
    print("the humidity in hong kong is high")
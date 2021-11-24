import datetime
from pytz import timezone
from astral import LocationInfo
from astral.sun import sun
from collections import namedtuple
from calendar import monthrange

# precise timezone
def all_dates_in_year(year=2019):
	for month in range(1, 13): # Month is always 1..12
		for day in range(1, monthrange(year, month)[1] + 1):
	    		yield sun(city.observer, date=datetime.date(year, month, day), dawn_dusk_depression=6.0, tzinfo=timezone('Europe/Paris'))
	  
# here change the city you want (latitude and longitude above all)  		
city = LocationInfo("Rognonas", "France", "Europe/Paris", 43.8894592, 4.8037888)
#print((
#	f"Information for {city.name}/{city.region}\n"
#	f"Timezone: {city.timezone}\n"
#	f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
#))
	    	
f = open("resultat.txt", "w")

# here change the year you want	
for date in all_dates_in_year(2020):
	print((
		f'Dawn:    {date["dawn"]}\n'
		# f'Sunrise: {date["sunrise"]}\n'
		# f'Noon:    {s["noon"]}\n'
		# f'Sunset:  {date["sunset"]}\n'
		f'Dusk:    {date["dusk"]}\n'
	))
	
	#############
	# Here adding 15 minutes before dawn and after dusk
	morning  = date["dawn"] - datetime.timedelta(minutes=15)
	afternoon  = date["dusk"] + datetime.timedelta(minutes=15)
	# 
	
	currentDay = str(morning.month).zfill(2)+str(morning.day).zfill(2)
	strMorning = str(morning.hour).zfill(2)+':'+str(morning.minute).zfill(2)
	strNight = str(afternoon.hour).zfill(2)+':'+str(afternoon.minute).zfill(2)
	
	output = currentDay+'|'+strMorning+'|'+strNight
	f.write(output+"\n")
f.close()

def address_to_coords(address):
	import requests
	key1 = 'AIzaSyAhQ0sPyYIxdsxrVOOmDONOoaxoXqGUiT4'
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	params1 = {'address':address,
				'key':key1}
	# todo check if request is error free
	r   = requests.get(url, params=params1).json()
	lat = r['results'][0]['geometry']['location']['lat']
	lon = r['results'][0]['geometry']['location']['lng']  
	print('The coordinates Of adress', address, ' is')
	print(lat,lon)
	return (lat,lon)

def coords_to_forecast(boolean_hourly,lat_lon_tuple):
	import forecastio as forec
	lat, lng = lat_lon_tuple  
	api_key = "0bfa820c54f7c641b1ca1efde7ed506e"
	#@todo make lat and lon as arguments
	f = forec.load_forecast(api_key, lat, lng)
	if boolean_hourly == True:
		r = f.hourly().summary	
	else:
		r = f.daily().summary
		
	print('The weather is .... tadaaa')
	print(r)
	return r
	#@todo rerun jupyter notebook


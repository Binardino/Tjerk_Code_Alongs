def from_address_to_weather(address):
	'''
	@input takes an address
	@output weather result

	@todo bla bla

	'''
	from coord_transformations import address_to_coords 
	from coord_transformations import coords_to_forecast 
	(lat,lon) = address_to_coords(address)
	result = coords_to_forecast(True, (lat,lon))
	return result


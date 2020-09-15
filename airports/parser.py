import json

countries_list = open('countries.csv','r').read().split('\n')
del countries_list[0]
del countries_list[-1]

countries = {}

for country in countries_list:
    countries[country.split(',')[1].strip('"')] = country.split(',')[2].strip('"')

airports_list = open('airports.csv','r').read().split('\n')
del airports_list[0]
del airports_list[-1]

airports = {}

with open('airports.json', 'a') as output_file:
    for airport in airports_list:
        airports['name'] = airport.split(',')[3].strip('"')
        airports['type'] = airport.split(',')[2].strip('"')
        airports['latitude'] = airport.split(',')[4].strip('"')
        airports['longitude'] = airport.split(',')[5].strip('"')
        airports['elevation_ft'] = airport.split(',')[6].strip('"')
        if airports['elevation_ft']:
            airports['elevation_mt'] = str(float(airports['elevation_ft']) * 0.3048)
        airports['continent'] = airport.split(',')[7].strip('"')
        airports['country_code'] = airport.split(',')[8].strip('"')
        airports['country_region'] = airport.split(',')[9].strip('"')
        airports['country_name'] = countries[airports['country_code']]
        airports['city'] = airport.split(',')[10].strip('"')
        airports['service'] = airport.split(',')[11].strip('"')
        airports['gps_code'] = airport.split(',')[12].strip('"')
        airports['iata_code'] = airport.split(',')[13].strip('"')
        airports['local_code'] = airport.split(',')[14].strip('"')
        json.dump(airports, output_file)
    
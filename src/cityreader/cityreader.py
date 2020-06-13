import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    """The City class object containing a name, latitude and longitude"""

    def __init__(self, name: str, lat: float, lon: float):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return f'City: {self.name}, {self.lat}, {self.lon}'

    def __repr__(self):
        return f'City({self.name}, {self.lat}, {self.lon})'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities: list = []) -> list:
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    fh = 'cities.csv'

    # Define the index of each row array in the csvreader object
    NAME_IDX = 0
    LAT_IDX = 3
    LON_IDX = 4

    # Open and read the csv file
    with open(fh, newline='') as csvfile:
        # Create the csvreader object to iterate over each line
        citiesreader = csv.reader(csvfile, delimiter=',')
        # Skip the header row, row 1 and build the city class objects
        # from the csv data and append to cities
        cities += [City(city[NAME_IDX], city[LAT_IDX], city[LON_IDX])
                   for city in list(citiesreader)[1:]]
    csvfile.close()  # close the file handle
    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
ip1 = input('Enter lat1,lon1: ')
ip2 = input('Enter lat2,lon2: ')
lat1, lon1 = ip1.split(',')
lat2, lon2 = ip2.split(',')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # Normalize input data
    lat1, lat2, lon1, lon2 = (float(lat1), float(lat2),
                              float(lon1), float(lon2))
    if lon1 < lon2:
        left_lon = lon2
        left_lat = lat2
        right_lon = lon1
        right_lat = lat1
    else:
        left_lon = lon1
        left_lat = lat1
        right_lon = lon2
        right_lat = lat2

    # Go through each city and check to see if it falls within
    # the specified coordinates.
    cities_in_lat = [city for city in cities if
                     right_lat <= city.lat <= left_lat]
    cities_in_lon = [city for city in cities if
                     right_lon <= city.lon <= left_lon]

    # Get the intersection
    # Note: Using set intersection would have been cleaner, but the test object
    # is not sorted, so using an unordered collection wouldn't pass the test
    within += [city for city in cities_in_lat if city in cities_in_lon]
    return within


# Manually test the cityreader_stretch function
cities_within = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
print('\n'.join([str(city) for city in cities_within]))

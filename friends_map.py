'''
The following module receives a .json file and modifies it into a DataFrame
with all additional information (coordinates based on locations).
'''

from geopy import Nominatim
from geopy.exc import GeocoderUnavailable
import pandas as pd


def gen_location(location: str):
    '''
    The function returns latitude and longitude of the entered location.
    '''
    try:
        geolocator = Nominatim(user_agent='tito').geocode(location)
        data = (geolocator.latitude, geolocator.longitude)
    except AttributeError:
        data = (0, 0)
    except GeocoderUnavailable:
        data = (0, 0)

    return data


def find_locations(json_f):
    '''
    The following function reads a .json file, takes out locations, nicknames
    of user's followers on Twitter and returns a DataFrame with filtered info.
    '''

    result = []
    for elem in json_f['users']:

        name = elem["screen_name"]
        location = elem["location"]
        if location != '':
            coordinates = gen_location(location)

            result.append([name, location, coordinates])

    result = pd.DataFrame(result)

    result.columns = ['Nickname', 'Location', 'Coordinates']
    result['Lat'] = result['Coordinates'].apply(lambda x: x[0])
    result['Lon'] = result['Coordinates'].apply(lambda x: x[1])

    return result


if __name__ == "__main__":
    pass

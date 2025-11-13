
import os

import requests
from models.contact import Contact


def get_data():
    requestUrl = os.environ.get("OPENSKY_NETWORK_API_BASE_URL") + "states/all"
    response = requests.get(requestUrl).json()
    contacts = []
    for state in response['states']:
        icao24 = state[0]
        callsign = state[1]
        origin_country = state[2]
        time_position = state[3]
        last_contact = state[4]
        longitude = state[5]
        latitude = state[6]
        baro_altitude = state[7]
        on_ground = state[8]
        velocity = state[9]
        true_track = state[10]
        vertical_rate = state[11]
        sensors = state[12]
        geo_altitude = state[13]
        squawk = state[14]
        spi = state[15]
        position_source = state[16]
        category = state[17] if len(state) > 17 else None
        contact = Contact(
            icao24, 
            callsign, 
            origin_country, 
            time_position, 
            last_contact, 
            longitude, 
            latitude, 
            baro_altitude, 
            on_ground, 
            velocity, 
            true_track, 
            vertical_rate, 
            sensors, 
            geo_altitude, 
            squawk, 
            spi, 
            position_source, 
            category
        )
        contacts.append(contact)
    return contacts
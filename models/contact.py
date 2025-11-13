
class Contact:
    def __init__(
            self, 
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
        ):
        self.icao24 = icao24
        self.callsign = callsign
        self.origin_country = origin_country
        self.time_position = time_position
        self.last_contact = last_contact
        self.longitude = longitude
        self.latitude = latitude
        self.baro_altitude = baro_altitude
        self.on_ground = on_ground
        self.velocity = velocity
        self.true_track = true_track
        self.vertical_rate = vertical_rate
        self.sensors = sensors
        self.geo_altitude = geo_altitude
        self.squawk = squawk
        self.spi = spi
        self.position_source = position_source
        self.category = category

    def __repr__(self):
        return(
            f"\n\n"
            f"Contact( \n" + 
            f"icao24={self.icao24}, \n" +
            f"callsign={self.callsign}, \n" +
            f"origin_country={self.origin_country}, \n" +
            f"time_position={self.time_position}, \n" +
            f"last_contact={self.last_contact}, \n" +
            f"longitude={self.longitude}, \n" +
            f"latitude={self.latitude}, \n" + 
            f"baro_altitude={self.baro_altitude}, \n" + 
            f"on_ground={self.on_ground}, \n" + 
            f"velocity={self.velocity}, \n" +
            f"true_track={self.true_track}, \n" + 
            f"vertical_rate={self.vertical_rate}, \n"
            f"sensors={self.sensors}, \n" +
            f"geo_altitude={self.geo_altitude}, \n" +
            f"squawk={self.squawk},\n" +
            f"spi={self.spi}, \n" +
            f"position_source={self.position_source}, \n" +
            f"category={self.category} \n" + 
            f")"
        )
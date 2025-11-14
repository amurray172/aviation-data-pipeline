
from dataclasses import dataclass, field


@dataclass
class Contact:
    icao24: str # Unique ICAO 24-bit address of the transponder in hex string representation.
    callsign: str # Callsign of the vehicle (8 chars). Can be None if no callsign has been received.
    origin_country: str # Country name inferred from the ICAO 24-bit address.
    time_position: int | None # Unix timestamp (seconds) for the last position update. None if no position report was received.
    last_contact: int # Unix timestamp (seconds) for the last update in general.
    longitude: float | None # WGS-84 longitude in decimal degrees. None if no position report was received.
    latitude: float | None # WGS-84 latitude in decimal degrees. None if no position report was received.
    baro_altitude: float | None # Barometric altitude in meters. None if no altitude report was received.
    on_ground: bool # True if the position was retrieved from a surface position report.
    velocity: float | None # Velocity over ground in m/s. None if no velocity report was received.
    true_track: float | None # True track in decimal degrees clockwise from north. None if no track report was received.
    vertical_rate: float | None # Vertical rate in m/s. None if no vertical rate report was received.
    sensors: list[int] | None # List of sensor IDs which contributed to this state vector. None if no sensor information is available.
    geo_altitude: float | None # Geometric altitude in meters. None if no altitude report was received.
    squawk: str | None # Transponder code (Squawk). None if no transponder code has been received.
    spi: bool # Special Position Indicator.
    position_source: int # Origin of this state vector: 0 = ADS-B, 1 = ASTERIX, 2 = MLAT
    category: int | None # Category of the vehicle as defined by the transponder. None if no category information is available.

    position_source_dict = {
        0: "ADS-B",
        1: "ASTERIX",
        2: "MLAT",
        3: "FLARM",
    }
    category_dict = {
        0: "No information",
        1: "No ADS-B Emitter Category Information",
        2: "Light (<15500 lbs)", 
        3: "Small (15500 to 75000 lbs)",
        4: "Large (75000 to 300000 lbs)",
        5: "High Vortex Large (aircraft such as B-757)",
        6: "Heavy (>300000 lbs)",
        7: "High Performance (>5g acceleration and >400 kts)",
        8: "Rotorcraft",
        9: "Glider / Sailplane",
        10: "Lighter-than-air",
        11: "Parachutist / Skydiver",
        12: "Ultralight / Hang-glider / Paraglider",
        13: "Reserved",
        14: "Unmanned Aerial Vehicle",
        15: "Space / Trans-Atmospheric Vehicle",
        16: "Surface Vehicle - Emergency Vehicle",
        17: "Surface Vehicle - Service Vehicle",
        18: "Point Obstacle (includes tethered balloons)",
        19: "Cluster Obstacle",
        20: "Line Obstacle",
    }

    position_source_name: str | None = field(init=False)
    category_name: str | None = field(init=False)


    def __post_init__(self):
        self.category_name = (
            self.category_dict.get(self.category, "Unknown Category")
            if self.category is not None
            else None
        )
        self.position_source_name = (
            self.position_source_dict.get(self.position_source, "Unknown Source")
            if self.position_source is not None
            else None
        )


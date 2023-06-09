"""

"""

class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = None
        self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude
    
    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if -90 <= lat_value <= 90:
            self._latitude = lat_value
        else:
            raise ValueError(
                f"{lat_value} is an invalid value for latitude"
            )
    
    @property
    def longitude(self) -> float:
        return self._longitude
    
    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if -180 <= long_value <= 180:
            self._longitude = long_value
        else:
            raise ValueError(
                f"{long_value} is an invalid value for longitude"
            )
        
if __name__ == "__main__":
    coordinate = Coordinate(lat=0, long=0)
    print(coordinate.latitude)
    print(coordinate.longitude)

    coordinate.latitude = 90
    coordinate.longitude = 110
    print(coordinate.latitude)
    print(coordinate.longitude)
from dataclasses import dataclass

@dataclass
class WeatherObservation:
    precip: float
    temp: float
    wind: float

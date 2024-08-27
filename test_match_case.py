from dataclasses import dataclass

@dataclass
class Point:
    lat: float
    lon: float

@dataclass
class Location:
    name: str
    error: float
    point: Point
    metadata: str = ""

def match_simple_pattern(loc: Location) -> None:
    match loc:
        case Location(str(name), float(error), Point(float(lat), float(lon)) as the_point) as captured_loc if error == 0 and lat == 127.8:
            print("This is the intial point", captured_loc, the_point)
        case Location(_, _, Point(_, _) as the_point, str(metadata)) as captured_loc if metadata:
            print("Location with metadata", captured_loc, the_point)
        case _:
            print("Unknown point!")

if __name__ == "__main__":
    initial = Location("initial", 0.0, Point(127.8, 3.14))
    initial = Location("initial", 0.0, Point(0.8, 3.14), "The greatest metadata")
    match_simple_pattern(initial)

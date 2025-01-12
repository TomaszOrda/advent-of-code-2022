from re import findall
from dataclasses import dataclass
from itertools import product


@dataclass
class SensorEdgeFunction:
    a: int
    b: int

    def intersection(self, other: "SensorEdgeFunction") -> (tuple[int, int] | None):
        """
        ax + b = cx + d \n
        x(a-c) = d - b \n
        x = (d - b) / (a - c) \n
        """
        if self.a != other.a:
            x = (other.b - self.b) // (self.a - other.a)
            y = self.a * x + self.b
            return (x, y)
        else:
            return None


class Sensor:
    def __init__(self, sensor_report) -> None:
        coords = [int(coord) for coord in findall(r'\-*\d+', sensor_report)]
        self.position = (coords[0], coords[1])
        self.exclusion_distance = manhattan_distance((coords[0], coords[1]), (coords[2], coords[3]))


def edges(sensor):
    left = sensor.position[0] - sensor.exclusion_distance - 1
    right = sensor.position[0] + sensor.exclusion_distance + 1
    y = sensor.position[1]
    for a in [1, -1]:
        for x in [left, right]:
            # ax + b = y; b = y - ax
            yield SensorEdgeFunction(a, y - a*x)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def frequency(beacon):
    return (beacon[0]) * 4_000_000 + beacon[1]


def excluded(sensors, max_coordinate, candidate):
    in_bounds = 0 <= candidate[0] <= max_coordinate and 0 <= candidate[1] <= max_coordinate
    return not in_bounds or \
        any(manhattan_distance(candidate, sensor.position) <= sensor.exclusion_distance for sensor in sensors)


def solution(raw_input: str):
    sensors = [
        Sensor(report)
        for report in raw_input.splitlines()
        ]
    max_coordinate = 4_000_000 if len(sensors) > 20 else 20

    for sensor_1, sensor_2 in product(sensors, repeat=2):
        for edge_1, edge_2 in product(edges(sensor_1), edges(sensor_2)):
            candidate = edge_1.intersection(edge_2)
            if candidate and not excluded(sensors, max_coordinate, candidate):
                return frequency(candidate)

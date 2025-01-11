from re import findall


def border(sensor):
    result = set()
    sensor_x, sensor_y = sensor['position']
    distance = sensor['exclusion_distance'] + 1
    for offset_x in range(0, distance):
        offset_y = distance - offset_x
        result.add((sensor_x + offset_x, sensor_y + offset_y))
        result.add((sensor_x + offset_x, sensor_y - offset_y))
        result.add((sensor_x - offset_x, sensor_y + offset_y))
        result.add((sensor_x - offset_x, sensor_y - offset_y))
    return result


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def frequency(beacon):
    print(beacon)
    return (beacon[0]) * 4_000_000 + beacon[1]


def solution(raw_input: str):
    sensor_beacon_pairs = [
        [int(coord) for coord in findall(r'\-*\d+', line)]
        for line in raw_input.splitlines()
        ]
    sensors = [
        {
            'position': (sensor[0], sensor[1]),
            'exclusion_distance': manhattan_distance((sensor[0], sensor[1]), (sensor[2], sensor[3]))
        }
        for sensor in sensor_beacon_pairs
    ]
    max_coordinate = 4_000_000 if len(sensors) > 20 else 20

    for center_sensor in sensors:
        for candidate in border(center_sensor):
            if candidate[0] <= max_coordinate and \
                    candidate[0] >= 0 and \
                    candidate[1] <= max_coordinate and \
                    candidate[1] >= 0:
                if all(manhattan_distance(candidate, sensor['position']) > sensor['exclusion_distance']
                       for sensor in sensors):
                    return frequency(candidate)

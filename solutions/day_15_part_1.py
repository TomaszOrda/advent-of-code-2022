from re import findall


def solution(raw_input: str):
    sensors = [
        tuple(int(coord) for coord in findall(r'\-*\d+', line))
        for line in raw_input.splitlines()
        ]

    row_to_check = 2_000_000 if len(sensors) > 20 else 10
    excluded_zones = set()

    for sensor in sensors:
        distance_max = abs(sensor[0] - sensor[2])+abs(sensor[1] - sensor[3])
        distance_to_the_row_to_check = abs(sensor[1] - row_to_check)
        distace_left = max(0, distance_max-distance_to_the_row_to_check)
        excluded_zones.update(set(range(sensor[0] - distace_left, sensor[0] + distace_left)))

    for sensor in sensors:
        if sensor[3] == row_to_check:
            excluded_zones.add(sensor[2])
        if sensor[1] == row_to_check:
            excluded_zones.add(sensor[0])

    return len(excluded_zones)

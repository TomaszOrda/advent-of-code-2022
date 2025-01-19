from enum import Enum
from math import ceil

MINUTES = 24


class OreTypes(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


class Robot:
    def __init__(self, variant, cost) -> None:
        self.variant = variant
        self.cost = cost

    def can_produce(self, robots):
        return all(ore_cost == 0 or robot_count > 0 for ore_cost, robot_count in zip(self.cost, robots))

    def time_to_produce(self, robots, ores):
        return max(
            ceil(max(0, (ore_cost - ore)) / robot_count)
            for ore_cost, ore, robot_count in zip(self.cost, ores, robots)
            if ore_cost > 0
        ) + 1


class Blueprint:
    def __init__(self, blueprint_string: str) -> None:
        blueprint_values = [
            int(value)
            for value in blueprint_string.replace(":", "").split(' ')
            if value.isnumeric()
        ]

        self.id = blueprint_values[0]
        self.robots = {
            OreTypes.ORE: Robot(OreTypes.ORE, [blueprint_values[1],
                                               0,
                                               0,
                                               0]),
            OreTypes.CLAY: Robot(OreTypes.CLAY, [blueprint_values[2],
                                                 0,
                                                 0,
                                                 0]),
            OreTypes.OBSIDIAN: Robot(OreTypes.OBSIDIAN, [blueprint_values[3],
                                                         blueprint_values[4],
                                                         0,
                                                         0]),
            OreTypes.GEODE: Robot(OreTypes.GEODE, [blueprint_values[5],
                                                   0,
                                                   blueprint_values[6],
                                                   0])
        }
        self.max_ore_cost = [max(robot.cost[i] for robot in self.robots.values()) for i in range(0, 4)]
        self.max_production_found = False
        self.max_production = 0

    def find_maximum_production(self):
        self.find_maximum_production_aux(time_left=MINUTES, robots=[1, 0, 0, 0], ores=[0, 0, 0, 0])
        self.max_production_found = True
        return self.max_production

    def find_maximum_production_aux(self, time_left, robots, ores):
        current_geode_forecast = ores[-1] + time_left * robots[-1]
        self.max_production = max(self.max_production, current_geode_forecast)

        if current_geode_forecast + time_left * (time_left - 1) // 2 < self.max_production:
            return None

        next_steps = []
        for ore_type in reversed(OreTypes):
            if ore_type != OreTypes.GEODE and self.max_ore_cost[ore_type.value] <= robots[ore_type.value]:
                continue
            if self.robots[ore_type].can_produce(robots):
                time_to_produce = self.robots[ore_type].time_to_produce(robots, ores)
                if time_left - time_to_produce >= 0:
                    new_time = time_left - time_to_produce
                    new_robots = robots[:]
                    new_robots[ore_type.value] += 1
                    new_ores = [
                        z[0] + time_to_produce * z[1] - z[2]
                        for z in zip(ores, robots, self.robots[ore_type].cost)
                    ]
                    next_steps.append((new_time, new_robots, new_ores))
        for args in next_steps:
            self.find_maximum_production_aux(*args)

    def quality(self):
        if not self.max_production_found:
            self.find_maximum_production()
        return self.id * self.max_production


def solution(raw_input: str):
    blueprints = [
        Blueprint(blueprint_string) for blueprint_string in raw_input.splitlines()
    ]

    return sum(blueprint.quality() for blueprint in blueprints)

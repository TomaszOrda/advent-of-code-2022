from collections import deque


class Valve:
    def __init__(self, valve_scan: str) -> None:
        scan_data = valve_scan.replace(",", "").split(' ')
        self.id = scan_data[1]
        self.flow_rate = int(scan_data[4].strip("rate=;"))
        self.tunnels = scan_data[9:]


class VolcanoComplex:
    def __init__(self, raw_input) -> None:
        self.valves = {valve.id: valve for valve in (Valve(valve_scan) for valve_scan in raw_input.splitlines())}
        self.flow_valves = [valve.id for valve in self.valves.values() if valve.flow_rate > 0]
        self.shortest_path = {valve.id: self.shortest_paths(valve) for valve in self.valves.values()}
        self.cache = {}

    def shortest_paths(self, starting_valve: "Valve"):
        queue = deque([starting_valve.id])
        distances = {starting_valve.id: 0}
        while queue:
            valve = self.valves[queue.pop()]
            for next_valve in valve.tunnels:
                if next_valve not in distances or distances[valve.id] + 1 < distances[next_valve]:
                    distances[next_valve] = distances[valve.id] + 1
                    queue.appendleft(next_valve)
        del distances[starting_valve.id]
        return distances

    def max_flow_rate(self, start_valve, visited_valves: set[str], time_left=30):
        cache_key = (
            start_valve,
            ''.join(sorted(list(visited_valves))),
            # tuple(True if flow_valve in visited_valves else False for flow_valve in self.flow_valves),
            time_left
        )
        if cache_key in self.cache:
            return self.cache[cache_key]

        possible_flows = [0]
        for next_valve in self.flow_valves:
            if next_valve not in visited_valves:
                new_time_left = time_left - 1 - self.shortest_path[start_valve][next_valve]
                if new_time_left > 0:
                    additional_flow = new_time_left * self.valves[next_valve].flow_rate
                    remaining_flow = self.max_flow_rate(
                        next_valve,
                        visited_valves.union([next_valve]),
                        new_time_left)
                    possible_flows.append(additional_flow + remaining_flow)
        self.cache[cache_key] = max(possible_flows)
        return self.cache[cache_key]


def solution(raw_input: str):
    volcano_complex = VolcanoComplex(raw_input)
    return volcano_complex.max_flow_rate("AA", set())

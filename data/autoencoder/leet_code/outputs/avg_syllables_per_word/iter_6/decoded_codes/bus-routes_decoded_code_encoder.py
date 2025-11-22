from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_index)

        bus_queue = deque()
        visited_buses = set()
        visited_stops = set([source])

        for bus in stop_to_buses[source]:
            bus_queue.append((bus, 1))
            visited_buses.add(bus)

        while bus_queue:
            current_bus, bus_count = bus_queue.popleft()
            for stop in routes[current_bus]:
                if stop == target:
                    return bus_count
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_bus in stop_to_buses[stop]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            bus_queue.append((next_bus, bus_count + 1))
        return -1
from collections import deque, defaultdict

def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0

    stop_to_buses = defaultdict(list)
    for bus, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(bus)

    bus_queue = deque((bus, 1) for bus in stop_to_buses[source])
    visited_buses = set(bus for bus, _ in bus_queue)
    visited_stops = {source}

    while bus_queue:
        bus, count = bus_queue.popleft()
        for stop in routes[bus]:
            if stop == target:
                return count
            if stop not in visited_stops:
                visited_stops.add(stop)
                for nxt_bus in stop_to_buses[stop]:
                    if nxt_bus not in visited_buses:
                        visited_buses.add(nxt_bus)
                        bus_queue.append((nxt_bus, count + 1))

    return -1
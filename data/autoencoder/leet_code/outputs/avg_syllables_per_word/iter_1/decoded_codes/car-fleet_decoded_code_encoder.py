def carFleet(target, cars):
    cars.sort(key=lambda x: x[0], reverse=True)
    times = [(target - pos) / speed for pos, speed in cars]
    fleets = 0
    max_time = 0
    for t in times:
        if t > max_time:
            fleets += 1
            max_time = t
    return fleets
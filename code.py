from collections import defaultdict, deque

def numBusesToDestination(routes, S, T):
    if S == T:
        return 0
    stop_to_buses = defaultdict(list)
    for bus_id, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(bus_id)
    
    start_buses = set(stop_to_buses.get(S, []))
    target_buses = set(stop_to_buses.get(T, []))
    
    if start_buses & target_buses:
        return 1
    
    visited = set(start_buses)
    queue = deque([(bus, 1) for 
# Question 24: Minimum number of platforms needed for a railway station problem.

def min_platforms_optimal(arrivals, departures):
    events = []
    for i in range(len(arrivals)):
        events.append((arrivals[i], 1))  # 1 for arrival
        events.append((departures[i], -1))  # -1 for departure

    events.sort() # Sort by time, then by event type (departure before arrival)
    # print(events)

    platforms_needed = 0
    max_platforms = 0

    for _, event_type in events:
        platforms_needed += event_type
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms


arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

print(min_platforms_optimal(arrivals, departures))
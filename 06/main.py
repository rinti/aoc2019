from collections import defaultdict
from functools import reduce

inputs = [x.strip() for x in open("./input.txt").readlines()]

planets = defaultdict(list)

for orbit in inputs:
    planet, orbit = orbit.split(")")
    planets[planet].append(orbit)

def count(obj):
    if obj not in planets:
        return 0

    children = planets[obj]
    return len(children) + sum(map(count, children))

print(sum(map(count, planets.keys())))

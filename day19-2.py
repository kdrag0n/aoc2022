#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0
import re
bps=[]
while True:
    for l in file_lines:
        matches = re.findall(r'(\d+)', l)
        bpid, ore_cost, clay_cost, obs_cost1, obs_cost2, geo_cost1, geo_cost2 = ints(matches)
        bps.append((ore_cost, clay_cost, obs_cost1, obs_cost2, geo_cost1, geo_cost2))


        if False:
            total += 1

    break
bps=bps[:3]
# print(bps)
# def run_bp(bp):
#     ore_cost, clay_cost, obs_cost1, obs_cost2, geo_cost1, geo_cost2 = bp
#     ores, clays, obs, geos = 0, 0, 0, 0
#     orebots, claybots, obsbots, geobots = 1, 0, 0, 0
#     for time in range(1, 25):
#         print(f'min {time}')
#         to_add_orebots = 0
#         to_add_claybots = 0
#         to_add_obsbots = 0
#         to_add_geobots = 0
#         if ores >= geo_cost1 and obs >= geo_cost2:
#             print(f'  build geo')
#             ores -= geo_cost1
#             obs -= geo_cost2
#             to_add_geobots += 1
#         elif ores >= obs_cost1 and clays >= obs_cost2:
#             print(f'  build obs')
#             ores -= obs_cost1
#             clays -= obs_cost2
#             to_add_obsbots += 1
#         elif ores >= clay_cost:
#             print(f'  build clay')
#             ores -= clay_cost
#             to_add_claybots += 1
#         elif ores >= ore_cost:
#             print(f'  build ore')
#             ores -= ore_cost
#             to_add_orebots += 1

#         print(f'  add: ores {orebots} clays {claybots} obs {obsbots} geos {geobots}')
#         ores += orebots
#         clays += claybots
#         obs += obsbots
#         geos += geobots

#         print(f'  newly built: ores {to_add_orebots} clays {to_add_claybots} obs {to_add_obsbots} geos {to_add_geobots}')
#         orebots += to_add_orebots
#         claybots += to_add_claybots
#         obsbots += to_add_obsbots
#         geobots += to_add_geobots

#         print(f'  state: ores {ores} clays {clays} obs {obs} geos {geos}')
    
#     print('FINAL', geos)

# for i, bp in enumerate(bps):
#     print(i)
#     run_bp(bp)
# run_bp(bps[0])
ore_cost, clay_cost, obs_cost1, obs_cost2, geo_cost1, geo_cost2 = bps[1]
maxore = max(ore_cost, clay_cost, obs_cost1, geo_cost1)
maxclay = obs_cost2
maxobs = geo_cost2
def run_step(time, ores, clays, obs, geos, orebots, claybots, obsbots, geobots):
    if time == 32: return geos
    #print(f'min {time}')
    maxr = -100
    if ores >= geo_cost1 and obs >= geo_cost2:
        #print(f'  build geo')
        return run_step(time+1, ores-geo_cost1+orebots, clays+claybots, obs-geo_cost2+obsbots, geos+geobots, orebots, claybots, obsbots, geobots+1)
    if ores >= obs_cost1 and clays >= obs_cost2 and obsbots < maxobs:
        #print(f'  build obs')
        ret = run_step(time+1, ores-obs_cost1+orebots, clays-obs_cost2+claybots, obs+obsbots, geos+geobots, orebots, claybots, obsbots+1, geobots)
        #if ret > maxr: maxr = ret
        return ret
    if ores >= clay_cost and claybots < maxclay:
        #print(f'  build clay')
        ret = run_step(time+1, ores-clay_cost+orebots, clays+claybots, obs+obsbots, geos+geobots, orebots, claybots+1, obsbots, geobots)
        if ret > maxr: maxr = ret
    if ores >= ore_cost and orebots < maxore:
        #print(f'  build ore')
        ret = run_step(time+1, ores-ore_cost+orebots, clays+claybots, obs+obsbots, geos+geobots, orebots+1, claybots, obsbots, geobots)
        if ret > maxr: maxr = ret
    # do nothing
    ret = run_step(time+1, ores+orebots, clays+claybots, obs+obsbots, geos+geobots, orebots, claybots, obsbots, geobots)
    if ret > maxr: maxr = ret
    return maxr

#print(run_step(0, 0, 0, 0, 0, 1, 0, 0, 0))
total=1
for i,bp in enumerate(bps):
    bpid=i+1
    print('bp',bpid)
    ore_cost, clay_cost, obs_cost1, obs_cost2, geo_cost1, geo_cost2 = bp
    maxore = max(ore_cost, clay_cost, obs_cost1, geo_cost1)
    maxclay = obs_cost2
    maxobs = geo_cost2
    geode = run_step(0, 0, 0, 0, 0, 1, 0, 0, 0)
    total*=geode
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

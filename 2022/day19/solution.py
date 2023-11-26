import re
import functools

with open("input") as f:
    inp = f.read().strip().split("\n")


def solve(time_stop, ore_rob_ore, clay_rob_ore, obs_rob_ore, obs_rob_clay, geo_rob_ore, geo_rob_obs):

    @functools.cache
    def max_geode(resources, robots, time):
        ore, clay, obs, geo = resources
        rob1, rob2, rob3, rob4 = robots
        if time == time_stop:
            return geo
        
        # Looking at the input, we notice that we can at most use 4 ore, 20 clay and 20 obsidian per turn. Hence there is
        # no need to collect more resources that we can spend given the remaining time.
        # We truncate the resources at the maximum quantity that we can spend to reduce the search space.
        ore_max_use = 4*(time_stop-time)
        ore_will_get = rob1*(time_stop-time-1)
        ore = min(ore, ore_max_use-ore_will_get)
        
        clay_max_use = 20*(time_stop-time)
        clay_will_get = rob2*(time_stop-time-1)
        clay = min(clay, clay_max_use-clay_will_get)
        
        obs_max_use = 20*(time_stop-time)
        obs_will_get = rob3*(time_stop-time-1)
        obs = min(obs, obs_max_use-obs_will_get)
        
        # If we can buy a geode bot, we should probably do so.
        if ore >= geo_rob_ore and obs >= geo_rob_obs:
            new_res = (ore+rob1-geo_rob_ore, clay+rob2, obs+rob3-geo_rob_obs, geo+rob4)
            new_robots = (rob1, rob2, rob3, rob4+1)
            return(max_geode(new_res, new_robots, time+1))

        best = 0
        # Buy nothing.
        best = max(best, max_geode((ore+rob1, clay+rob2, obs+rob3, geo+rob4), robots, time+1))
        
        # Buy ore robot.
        if ore >= ore_rob_ore:
            new_res = (ore+rob1-ore_rob_ore, clay+rob2, obs+rob3, geo+rob4)
            new_robots = (rob1+1, rob2, rob3, rob4)
            best = max(best, max_geode(new_res, new_robots, time+1))

        # Buy clay robot.
        if ore >= clay_rob_ore:
            new_res = (ore+rob1-clay_rob_ore, clay+rob2, obs+rob3, geo+rob4)
            new_robots = (rob1, rob2+1, rob3, rob4)
            best = max(best, max_geode(new_res, new_robots, time+1))
            
        # Buy obsidian robot.
        if ore >= obs_rob_ore and clay >= obs_rob_clay:
            new_res = (ore+rob1-obs_rob_ore, clay+rob2-obs_rob_clay, obs+rob3, geo+rob4)
            new_robots = (rob1, rob2, rob3+1, rob4)
            best = max(best, max_geode(new_res, new_robots, time+1))
        
        # Buy geode robot.
        if ore >= geo_rob_ore and obs >= geo_rob_obs:
            new_res = (ore+rob1-geo_rob_ore, clay+rob2, obs+rob3-geo_rob_obs, geo+rob4)
            new_robots = (rob1, rob2, rob3, rob4+1)
            best = max(best, max_geode(new_res, new_robots, time+1))

        return best

    return max_geode((0,0,0,0), (1,0,0,0), 0)  


# Part 1
quality = 0
for i, line in enumerate(inp):
    index, ore_rob_ore, clay_rob_ore, obs_rob_ore, obs_rob_clay, geo_rob_ore, geo_rob_obs = map(int, re.findall("\d+", line))
    res = solve(24, ore_rob_ore, clay_rob_ore, obs_rob_ore, obs_rob_clay, geo_rob_ore, geo_rob_obs)
    quality += res*(i+1)

print(quality)

# Part 2
prod = 1
for i, line in enumerate(inp[:3]):
    index, ore_rob_ore, clay_rob_ore, obs_rob_ore, obs_rob_clay, geo_rob_ore, geo_rob_obs = map(int, re.findall("\d+", line))
    res = solve(32, ore_rob_ore, clay_rob_ore, obs_rob_ore, obs_rob_clay, geo_rob_ore, geo_rob_obs)
    prod *= res

print(prod)
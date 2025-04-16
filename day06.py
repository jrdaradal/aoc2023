# 2023 Advent of Code Day 06 Solution
# John Roy Daradal 

# SolutionA: 219849
# SolutionB: 29432455

from utils import *

def input06(full: bool) -> tuple[list[int], list[int]]:
    lines = readLines(getPath(6, full))
    times = [int(x) for x in lines[0].split(':')[1].strip().split()]
    bests = [int(x) for x in lines[1].split(':')[1].strip().split()]
    return (times, bests)

def day06A():
    full = True 
    times, bests = input06(full)
    total = 1
    for i,limit in enumerate(times):
        breakers = [True for x in computeOutcomes(limit) if x > bests[i]]
        total *= len(breakers)
    print(total)

def day06B():
    full = True 
    times, bests = input06(full)
    time = int(''.join(str(x) for x in times))
    best = int(''.join(str(x) for x in bests))
    breakers = [True for x in computeOutcomes(time) if x > best]
    print(len(breakers))

def computeOutcomes(limit: int) -> list[int]:
    outcomes = []
    for hold in range(limit+1):
        move = limit - hold 
        outcomes.append(move*hold)
    return outcomes 

if __name__ == '__main__':
    # day06A()
    day06B()
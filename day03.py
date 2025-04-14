# 2023 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 553079
# SolutionB: 84363105

import re
from utils import *

rowrange = tuple[int,int,int] # (row,col1,col2)

def input03(full: bool) -> list[str]:
    return readLines(getPath(3,full))

def day03A():
    full = True 
    grid = input03(full)
    symbols = findSymbols(grid) 
    total = sum(findValidNumbers(grid, symbols))
    print(total) 

def day03B():
    full = True 
    grid = input03(full)
    gears = findGears(grid)
    total = sum(findGearRatios(grid, gears))
    print(total)

NON_SYMBOL = '0123456789.'
def findSymbols(grid: list[str]) -> set[coords]:
    symbols: list[coords] = []
    for row,line in enumerate(grid):
        for col,char in enumerate(line):
            if char not in NON_SYMBOL:
                symbols.append((row,col))
    return set(symbols)

def findValidNumbers(grid: list[str], symbols:set[coords]) -> list[int]:
    bounds: coords = (len(grid),len(grid[0]))
    numbers: list[int] = []
    for row,line in enumerate(grid):
        for m in re.finditer(r'[0-9]+', line):
            start,end = m.start(), m.end()
            r = (row,start,end)
            if hasAdjacentSymbol(r, symbols, bounds):
                numbers.append(int(line[start:end]))
    return numbers

def findGears(grid: list[str]) -> set[coords]:
    gears: list[coords] = []
    for row,line in enumerate(grid):
        for col,char in enumerate(line):
            if char == '*':
                gears.append((row,col))
    return set(gears)

def findGearRatios(grid: list[str], gears: set[coords]) -> list[int]:
    bounds: coords = (len(grid),len(grid[0]))
    adjacent: dict[coords,list[int]] = {}
    for row,line in enumerate(grid):
        for m in re.finditer(r'[0-9]+', line):
            start,end = m.start(), m.end() 
            r = (row,start,end)
            number = int(line[start:end])
            for c in getAdjacentSymbols(r, gears, bounds):
                adjacent.setdefault(c, [])
                adjacent[c].append(number)

    numbers: list[int] = []
    for c in adjacent:
        if len(adjacent[c]) == 2:
            a,b = adjacent[c]
            numbers.append(a*b)
    return numbers 

def hasAdjacentSymbol(r: rowrange, symbols: set[coords], bounds: coords) -> bool:
    adjacent = getAdjacent(r, bounds)
    common = symbols.intersection(set(adjacent))
    return len(common) > 0

def getAdjacentSymbols(r: rowrange, symbols: set[coords], bounds: coords) -> list[coords]:
    adjacent = getAdjacent(r, bounds)
    common = symbols.intersection(set(adjacent))
    return sorted(common)

def getAdjacent(r: rowrange, bounds: coords) -> list[coords]:
    y,x1,x2  = r 
    numRows,numCols = bounds 
    prevY, nextY = y-1, y+1 
    prevX, nextX = x1-1, x2+1
    adjacent: list[coords] = []

    start = prevX if prevX >= 0 else x1 
    end = nextX if nextX <= numCols else x2
    addAbove = prevY >= 0
    addBelow = nextY < numRows 
    for col in range(start,end):
        if addAbove:
            adjacent.append((prevY,col))
        if addBelow:
            adjacent.append((nextY,col))
    if start != x1:
        adjacent.append((y,start))
    if x2 < numCols:
        adjacent.append((y,x2))
    return adjacent

if __name__ == '__main__':
    # day03A()
    day03B()
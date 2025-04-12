# 2023 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 55834

from utils import *

def input01(full: bool) -> list[str]:
    return readLines(getPath(1, full))

def day01A(): 
    full = True 
    total = 0 
    for line in input01(full):
        total += extractDigits(line)
    print(total)

def extractDigits(line: str) -> int:
    first, last = None, None 
    for x in line:
        digit = parseDigit(x)
        if digit != None:
            if first is None:
                first = digit 
            last = digit 
    return (first*10) + last

def parseDigit(x: str) -> int|None:
    code = ord(x)
    if 48 <= code and code <= 57:
        return code-48 
    return None

if __name__ == '__main__':
    day01A()
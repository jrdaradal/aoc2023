# 2023 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 55834
# SolutionB: 53221

from utils import *

def input01(full: bool) -> list[str]:
    return readLines(getPath(1, full))

def day01A(): 
    full = True 
    total = 0 
    for line in input01(full):
        total += extractDigits(line)
    print(total)

def day01B():
    full = True 
    total = 0 
    for line in input01(full):
        total += extractNumber(line)
    print(total)

def extractDigits(line: str) -> int:
    first, last = None, None 
    for x in line:
        digit = parseDigit(x)
        if digit != None:
            first,last = update(first,last,digit)
    return (first*10) + last

def extractNumber(line: str) -> int:
    first, last = None, None 
    for i in range(len(line)):
        digit = parseDigit(line[i])
        if digit != None:
            first,last = update(first,last,digit)
            continue 
        digit = parseNumber(line[i:])
        if digit != None:
            first,last = update(first,last,digit)
    return (first*10) + last

def parseDigit(x: str) -> int|None:
    code = ord(x)
    if 48 <= code and code <= 57:
        return code-48 
    return None

numberWords: tuple[str,int] = [
    ('one',1),('two',2),('three',3),('four',4),('five',5),
    ('six',6),('seven',7),('eight',8),('nine',9),
]

def parseNumber(text: str) -> int|None:
    for word,number in numberWords:
        if text.startswith(word):
            return number 
    return None

def update(first: int|None, last: int|None, digit: int) -> tuple[int,int]:
    if first is None:
        first = digit 
    last = digit 
    return (first, last)

if __name__ == '__main__':
    day01A()
    day01B()
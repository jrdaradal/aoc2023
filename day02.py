# 2023 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 2156
# SolutionB: 66909

from utils import *

draw = tuple[int,int,int]

class Game:
    def __init__(self,id: int):
        self.id = id 
        self.draws: list[draw] = []
    
    @property 
    def isValid(self) -> bool:
        for r,g,b in self.draws:
            if r > 12 or g > 13 or b > 14:
                return False 
        return True 
    
    @property 
    def power(self) -> int:
        maxR,maxG,maxB = 0,0,0 
        for r,g,b in self.draws:
            maxR = max(maxR,r)
            maxG = max(maxG,g)
            maxB = max(maxB,b)
        return maxR*maxG*maxB
    

def input02(full: bool) -> list[Game]:
    return [parseLine(x) for x in readLines(getPath(2, full))]

def day02A():
    full = True
    total = 0 
    for game in input02(full):
        if game.isValid:
            total += game.id 
    print(total)

def day02B():
    full = True 
    total = 0 
    for game in input02(full):
        total += game.power 
    print(total)

def parseLine(line: str) -> Game:
    head, tail = [x.strip() for x in line.split(':')]
    number = int(head.split()[1])
    game = Game(number)
    for d in tail.split(';'):
        game.draws.append(parseDraw(d))
    return game

def parseDraw(line: str) -> draw:
    r,g,b = 0,0,0 
    for part in line.split(','):
        number,color = [x.strip() for x in part.split()]
        number = int(number) 
        if color == 'red':
            r = number 
        elif color == 'green':
            g = number 
        elif color == 'blue':
            b = number 
    return (r,g,b)

if __name__ == '__main__':
    day02A()
    day02B()
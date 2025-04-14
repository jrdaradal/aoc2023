# 2023 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 26443

from utils import * 

game = tuple[set[int], set[int]] # winners, numbers

def input04(full: bool) -> list[game]:
    def convert(line: str) -> game:
        tail = line.split(':')[1]
        winners, numbers = tail.split('|')
        winners = getNumbers(winners)
        numbers = getNumbers(numbers)
        return (winners, numbers)
    return [convert(x) for x in readLines(getPath(4, full))]

def day04A():
    full = True 
    total = 0 
    for card in input04(full):
        total += computeScore(card)
    print(total)

def getNumbers(line: str) -> set[int]:
    return set(int(x.strip()) for x in line.strip().split())

def computeScore(card: game) -> int:
    winners, numbers = card 
    common = len(winners.intersection(numbers))
    if common == 0:
        return 0
    return 2 ** (common-1)

if __name__ == '__main__':
    day04A()
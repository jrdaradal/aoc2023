# 2023 Advent of Code Day 05 Solution
# John Roy Daradal 

# SolutionA: 403695602
# SolutionB: 219529182

from utils import * 

chain = ['seed','soil','fertilizer','water','light','temperature','humidity','location']
triple = tuple[int,int,int]
rangeMatch = tuple[int,int] | None


class Config: 
    def __init__(self):
        self.seeds: list[int] = []
        self.maps: dict[tuple[str,str], list[triple]] = {}

    @property 
    def seedRanges(self) -> list[tuple[int,int]]:
        s = self.seeds 
        return [(s[i],s[i]+s[i+1]-1) for i in range(0,len(s),2)]

    @property 
    def mapRanges(self) -> dict[tuple[str,str],list[triple]]:
        m = {}
        for key, items in self.maps.items():
            m[key] = []
            for src,dst,count in items:
                m[key].append((src,src+count-1,dst-src))
        return m

def input05(full: bool) -> Config:
    cfg = Config()
    key = None
    for line in readLines(getPath(5, full)):
        if line == '': continue 
        elif line.startswith('seeds:'):
            tail = line.split(':')[1].strip() 
            cfg.seeds = [int(x) for x in tail.split()]
        elif line.endswith('map:'):
            head = line.split()[0].strip()
            k1,k2 = head.split('-to-')
            key = (k1,k2)
            cfg.maps[key] = []
        else:
            dst,src,count = [int(x) for x in line.split()]
            cfg.maps[key].append((src,dst,count))
    return cfg

def day05A():
    full = True 
    cfg = input05(full)
    locations = applyMapChain(cfg)
    print(min(locations))

def day05B():
    full = True 
    cfg = input05(full)
    locations = applyMapRangeChain(cfg)
    print(min(locations))

def applyMapChain(cfg: Config) -> list[int]:
    current = cfg.seeds 
    for i in range(len(chain)-1):
        key = (chain[i],chain[i+1])
        current = translate(current, cfg.maps[key])
    return current 

def translate(numbers: list[int], t: list[triple]) -> list[int]:
    result: list[int] = []
    for x in numbers:
        y = x
        for src,dst,count in t:
            if src <= x and x < src + count:
                y = dst + (x-src)
                break 
        result.append(y)
    return result

def applyMapRangeChain(cfg: Config) -> list[int]:
    currRanges = cfg.seedRanges 
    rangeMap = cfg.mapRanges 
    for i in range(len(chain)-1):
        key = (chain[i],chain[i+1])
        nextRanges = []
        while len(currRanges) > 0:
            first, last = currRanges.pop(0)
            for rule in rangeMap[key]:
                delta = rule[2]
                if isInside(rule, first, last):
                    nextRanges.append((first+delta, last+delta))
                    break 
                match, extra = findIntersection(rule, first, last)
                if match != None:
                    first, last = match 
                    nextRanges.append((first+delta, last+delta))
                    currRanges.append(extra)
                    break
            else:
                nextRanges.append((first, last))
        currRanges = nextRanges
    return [x[0] for x in currRanges]

def isInside(rule: triple, first: int, last: int) -> bool:
    start, end, _ = rule 
    return start <= first and first <= last and last <= end

def findIntersection(rule: triple, first: int, last: int) -> tuple[rangeMatch, rangeMatch]:
    start, end, _ = rule 
    if start <= first and first <= end:
        match = (first,end)
        extra = (end+1,last)
    elif start <= last and last <= end:
        match = (start,last)
        extra = (first,start-1)
    else:
        match, extra = None, None 
    return match, extra

if __name__ == '__main__':
    # day05A()
    day05B()
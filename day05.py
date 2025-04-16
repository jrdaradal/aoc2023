# 2023 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 403695602

from utils import * 

chain = ['seed','soil','fertilizer','water','light','temperature','humidity','location']
triple = tuple[int,int,int]


class Config: 
    def __init__(self):
        self.seeds: list[int] = []
        self.maps: dict[tuple[str,str], list[triple]] = {}

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

if __name__ == '__main__':
    day05A()
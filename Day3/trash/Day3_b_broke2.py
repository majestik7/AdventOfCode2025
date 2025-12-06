
import os
import itertools
#import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
delim = ''

numlen = 15
combolen = 12

with open(inputfile, 'r') as file:
    for line in file:
        jolt = []
        line = line.strip()
        l = list(line)
        ordered = l.copy()
        ordered.sort()
        nl = line.count('1')
        n2 = ordered.count('1')

        while len(line) > numlen:
            a = int(line)
            b = int(line[1:])*10
            if a < b:
                line = line[1:]
            else:
                if len(ordered) > 0:
                    rm = ordered.pop(0)
                    if line.count(rm) > 0:
                        i = line.index(rm)
                        line = line[:i]+line[i+1:]
                else:
                    continue

        numbers = list(line)
        all_jolts = []
        for j in itertools.combinations(line, combolen):
            all_jolts.append(int(delim.join(j)))
        #print(all_jolts)
        maxjolt = max(all_jolts)
        
        print('\033[91m',maxjolt,'\033[0m')
        answer = answer + int(maxjolt)
        
print('\033[92m',answer,'\033[0m]')
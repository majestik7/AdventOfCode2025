
import os
import numpy as np

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0

with open(inputfile, 'r') as file:
    for line in file:
        
        line = line.strip()
        #print(line)
        idlist = line.split(',')
        #print(idlist)
        for rng in idlist:
            rng = list(map(int, rng.split('-')))
            #print(rng)
            ids = list(range(rng[0],rng[1]+1))
            #print(ids)
            for n in ids:
                if len(str(n)) % 2 == 0:
                    #print(n)
                    a = int(str(n)[:len(str(n))//2])
                    b = int(str(n)[len(str(n))//2:])
                    #print('a',a,' - b',b)
                    if a == b:
                        #print(a,b)
                        answer = answer + n

print(answer)
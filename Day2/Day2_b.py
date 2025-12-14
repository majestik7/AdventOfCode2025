
import os
import numpy as np

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0

def split_str_into_chunks(text, chunk_size):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks


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
                t = len(str(n))//2
                #print('t',t)
                for u in range(1,t+1):
                    #print(u)
                    chunk_res = split_str_into_chunks(str(n), u)
                    #print('chunk-',chunk_res)
                    if len(set(chunk_res)) == 1:
                        #print('\033[91mINVALID ID\033[0m',n)
                        answer = answer + n
                        break
                    

print(answer)
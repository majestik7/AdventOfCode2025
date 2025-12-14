
import os
import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\in_test.txt'

answer = 0

numlen = 2

def get_largest_index(list, string):
    for s in range(len(list) - 1, -1, -1):
        if list[s] == string:
            return s
    return -1

with open(inputfile, 'r') as file:
    for line in file:
        jolt = []
        line = line.strip()
        print(line)
        l = list(line)
        two = heapq.nlargest(2, l)
        print(two)
        l = [x for x in l if x in two]
        print(l)
        delim = ''
        if len(l) == numlen:
            jolt = delim.join(l)
        else:
            new = []
            for i in l:
                if i not in new:
                    new.append(i)
            newer = []
            nindx = []
            for n in new:
                nindx.append(get_largest_index(l, n))
            nindx.sort()
            for ni in nindx:
                newer.append(l[ni])
            jolt = delim.join(newer)
        print(jolt)
        answer = answer + int(jolt)


print(answer)
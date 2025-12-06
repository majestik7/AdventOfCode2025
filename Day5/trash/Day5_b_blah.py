
import os
import copy

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
fresh = []
all_fresh = []

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()
        if l.count('-') > 0:
            l = l.split('-')
            l = [int(item) for item in l]
            fresh.append(l)

all_fresh = copy.deepcopy(fresh)

changes = 1000
x = 0
es = 0
while es < 10:
    if changes < 1:
        es += 1
    #print('x',x)
    changes = 0
    while len(fresh) > 0:
        #print(fresh)
        f = fresh.pop(0)
        #print('f',f)
        for a in all_fresh:
            if f != a:
                print('a',a,'f',f, end=' ')
                if a[0] <= f[0] <= a[1]:
                    #print(a[0],'<=',f[0],'<',a[1])
                    if f[1] > a[1]:
                        a[1] = f[1]
                        changes += 1
                        print('a1 = f1')
                        break
                if a[0] <= f[1] <= a[1]:
                    #print(a[0],'<=',f[1],'<',a[1])
                    if f[0] < a[0]:
                        a[0] = f[0]
                        changes += 1
                        print('a0 = f0')
                        break
                if f[1] == a[1]:
                    print("LOOK HERE 0")
                    if f[0] < a[0]:
                        a[0] = f[0]
                        changes += 1
                        print('a0 = f0')
                        break
                if f[0] == a[0]:
                    print("LOOK HERE 0")
                    if f[1] < a[1]:
                        a[1] = f[1]
                        changes += 1
                        print('a1 = f1')
                        break
                print('NONE')
                        
    print('changes',changes)
    freshest =[]
    for fr in all_fresh:
        if fr not in freshest:
            freshest.append(fr)
    all_fresh = copy.deepcopy(freshest)
    fresh = copy.deepcopy(freshest)
    x += 1

all_fresh.sort(key=lambda x: x[0])
print(all_fresh)

for n in all_fresh:
    answer += n[1] - (n[0] - 1)

print('\033[92m',answer,'\033[0m')
import os
import copy
import math


current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\input.txt'

answer = 1
array = []
input = []
pairs = []
dists = []
circuits = []
connections = 1000

with open(inputfile, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(',')
        line = [int(s) for s in line]
        line = tuple(line)
        input.append(line)

def get_distance(point1,point2):
    x1,y1,z1 = point1[0],point1[1],point1[2]
    x2,y2,z2 = point2[0],point2[1],point2[2]
    sum3d = math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
    return sum3d

#print(input)
#print(get_distance(input[0],input[1]))
#x = 0
input2 = copy.deepcopy(input)
for a in input2:
    for b in input:
        #print('ab',a,b)
        #x += 1
        #if x % 1000 == 0:
        #    if len(dists) > 1000:
        #        dists = sorted(array, key=lambda item: item[-1])
        #        dists = dists[:1000]
        #print('b',x)
        if a != b:
            pair = sorted((a,b))
            if pair not in pairs:
                #print('working',pair)
                pairs.append((a,b))
                dist = get_distance(a,b)
                array.append([a,b,dist])
    #print('remove',a)
    input.remove(a)
    pairs = [item for item in pairs if a not in item]
        

dists = sorted(array, key=lambda item: item[-1])
print('dists was',len(dists),'long')
dists = dists[:connections]
print('dists was',len(dists),'long')

#for d in dists:
#    print(d[2],d[0],d[1])

x = 0
while len(dists) > 0:
    point_index = 'None'
    take = dists.pop(0)
    for sublist_index, sublist in enumerate(circuits):
        point_index = 'None'
        if take[0] in sublist:
            point_index = sublist.index(take[0])
            circuits[sublist_index].append(take[1])
            break
        if take[1] in sublist:
            point_index = sublist.index(take[1])
            circuits[sublist_index].append(take[0])
            break
            
    if point_index == 'None':
        circuits.append([take[0],take[1]])
    #else:
        #print(take,'found at',(sublist_index,point_index))
        

circuits = sorted(circuits, key=len, reverse=True)
#print(circuits)
circuits = circuits[:3]
x = 1
for c in circuits:
    print(x,len(c),c)
    answer = answer * len(c)
    x += 1
print('\n\033[92mAnswer:',answer,'\033[0m')
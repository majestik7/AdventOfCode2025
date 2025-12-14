import os
import copy
import math

current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\\input.txt'

answer = 0
array = []
input = []
pairs = []
red = []


with open(inputfile, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(',')
        line = [int(s) for s in line]
        line = tuple(line)
        input.append(line)

print('map1 complete')

xmin = sorted(input, key=lambda item: item[0])[0][0]
ymin = sorted(input, key=lambda item: item[1])[0][1]

for p in input:
    px = p[0] - xmin
    py = p[1] - ymin
    red.append((px+2,py+1))

def get_distance(point1,point2):
    x1,y1 = point1[0],point1[1]
    x2,y2 = point2[0],point2[1]
    sum3d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return sum3d

def get_area(point1,point2):
    area = (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)
    return area

red2 = copy.deepcopy(red)
for a in red2:
    for b in red:
        if a != b:
            pair = sorted((a,b))
            if pair not in pairs:
                pairs.append((a,b))
                areas = get_area(a,b)
                array.append([a,b,areas])
    red.remove(a)
    pairs = [item for item in pairs if a not in item]

areas = sorted(array, key=lambda item: item[-1])
print(areas[-1])
answer = areas[-1][-1]

print('\n\033[92mAnswer:',answer,'\033[0m')
import os
import copy
import math
import ast


current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\\intest.txt'

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
xmax = sorted(input, key=lambda item: item[0])[-1][0]
ymin = sorted(input, key=lambda item: item[1])[0][1]
ymax = sorted(input, key=lambda item: item[1])[-1][1]

xsub = xmin 
ysub = ymin

x = xmax-xmin+3
y = ymax-ymin+2

print(xmin,xmax,ymin,ymax)
print('remove',xsub,ysub)


for p in input:
    px = p[0] - xsub
    py = p[1] - ysub
    red.append((px+2,py+1))





#x = sorted(input, key=lambda item: item[0])[-1][0]+1
#y = sorted(input, key=lambda item: item[1])[-1][1]+1

print(x,y)
t_map = [['.'] * (x+2)] * (y+1)
t_map = str(t_map)
t_map = ast.literal_eval(t_map)            #dumbness to remove link of nested arrays

#for t in t_map:
#    print(t)

for coord in red:
    t_map[coord[1]][coord[0]] = '#'

print('Red Tiles added')

#for t in t_map:
#    print(t)

red2 = copy.deepcopy(red)
n = len(red2)
for a in red2:
    #print(n,'of',len(red2))
    n -= 1
    for b in red:
        if a != b:
            pair = sorted((a,b))
            if pair not in pairs:
                pairs.append(pair)
                #print('pr',pair)
                if pair[0][1] == pair[1][1]:
                    #print('y=',pair[0][1],pair[1][1])
                    for r in range(pair[0][0]+1,pair[1][0]):
                        #print(r)
                        if t_map[pair[0][1]][r] == '.':
                            t_map[pair[0][1]][r] = 'X'
                pair = sorted(pair, key=lambda item: item[0])
                if pair[0][0] == pair[1][0]:
                    #print('x=',pair[0][0],pair[1][0])
                    for r in range(pair[0][1],pair[1][1]):
                        #print(r)
                        if t_map[r][pair[0][0]] == '.':
                            t_map[r][pair[0][0]] = 'X'




for t in t_map:
    print(t)


fn = current_script_dir + f"\\map.txt"
fileout = open(fn, "w")
t_map = [str(item) + "\n" for item in t_map]
fileout.writelines(t_map)
fileout.close()



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
                #print('working',pair)
                pairs.append((a,b))
                areas = get_area(a,b)
                array.append([a,b,areas])
    #print('remove',a)
    red.remove(a)
    pairs = [item for item in pairs if a not in item]

areas = sorted(array, key=lambda item: item[-1])
#print(areas[-1])

#print(abs(dists[-1][0][0]-dists[-1][1][0]))
#print(abs(dists[-1][0][1]-dists[-1][1][1]))
#print('\n\033[92mAnswer:',area,'\033[0m')
import os
import operator
import copy


current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\input.txt'

answer = 0
array = []
input = []
start = "S"
delim = ''

with open(inputfile, 'r') as file:
    for line in file:
        line = list(line.strip())
        input.append(line)

array = copy.deepcopy(input)

def split_em(schimatic,pos):
        global answer,array
        r,c = pos[0],pos[1]
        if array[r][c] == start:
            if array[r+1][c] == '.':
                array[r+1][c] = '|'

        if array[r][c] == '.':
            if r > 0 and array[r-1][c] == '|':
                array[r][c] = "|"

        if array[r][c] == '^':
            if r > 0:
                if array[r-1][c] == '|':
                    answer += 1
            if c > 0:
                if array[r][c-1] != '|':
                    array[r][c-1] = '|'
            if c < len(array[r])-1:
                if array[r][c+1] != '|':
                    array[r][c+1] = '|'

def find_start(schematic):
    global start
    for r in range(len(schematic)):
        if start in schematic[r]:
            s_exist = schematic[r].index(start)
            if s_exist > 0:
                xy = (r,s_exist)
                return xy
            
start_loc = find_start(input)
print('start',start_loc)

for r in range(len(array)):
    for c in range(len(array[r])):
        pos = (r,c)
        split_em(array,pos)

#for a in array:
#    print(a)

print('\033[92mAnswer:',answer,'\033[0m')

#************************************  PART 2  ******************************

answer = 0
paths = []
start_a = []
start_a.append(start_loc)
paths.append(start_a)
#print(paths)

def map_paths(coords):
    global array, paths
    #print('coords',coords)
    for p in paths:
        p1 = p[-1]
        #print('p',p,'-1',p1,type(p1),'coords',coords,type(coords))
        new_path = []
        if p1 == coords:
            #print('continuing with', coords)
            if array[coords[0]][coords[1]] == '|' or array[coords[0]][coords[1]] == 'S':
                new_path = copy.deepcopy(p)
                #print('n1',new_path)
                new_path.append((coords[0]+1,coords[1]))
                #print('n2',new_path)
                if new_path not in paths:
                    paths.append(new_path)
                    #print('c',coords)
                if coords[0] < len(array)-1:
                    if array[coords[0]+1][coords[1]] == '^':
                        new_path2 = copy.deepcopy(new_path)
                        new_path2.append((coords[0]+1,coords[1]-1))
                        if new_path2 not in paths:
                            paths.append(new_path2)
                        new_path2 = copy.deepcopy(new_path)
                        new_path2.append((coords[0]+1,coords[1]+1))
                        if new_path2 not in paths:
                            paths.append(new_path2)
           


for r in range(len(array)):
    for c in range(len(array[r])):
        if array[r][c] != '.':
            map_paths((r,c))

#map_paths((0,7))

paths.sort()

#for a in range(len(array)):
#    print(array[a])
#    print(a)


for p in paths:
    #print(p)
    #print(p[-1][0])
    if p[-1][0] == len(array)-1:
        answer += 1

print('\033[92mAnswer2:',answer,'\033[0m')
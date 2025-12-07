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
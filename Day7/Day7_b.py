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

for i in range(0,len(input),2):
    array.append(input[i])

def split_em(y,x):
    global array
    if y == 0:
        return
    
    ch_self = array[y][x] == '^'
    ch_left = x != 0 and array[y][x-1] == '^'
    ch_right = x != len(array[y]) -1 and array[y][x+1] == '^'
    ch_top = y != 0 and array[y-1][x] == '^'

    if not ch_self and not ch_top:
        array[y][x] = array[y-1][x]

    if not ch_self and ch_left:
        array[y][x] += array[y-1][x-1]

    if not ch_self and ch_right:
        array[y][x] += array[y-1][x+1]


def find_start(schematic):
    global start
    for r in range(len(schematic)):
        if start in schematic[r]:
            s_exist = schematic[r].index(start)
            if s_exist > 0:
                xy = (r,s_exist)
                array[r][s_exist] = 1
                return xy
            
start_loc = find_start(input)
print('start',start_loc)

###############################   convert . to 0
for a in range(len(array)):
    for b in range(len(array[a])):
        if array[a][b] == '.':
            array[a][b] = 0

###############################   Print array
for r in range(len(array)):
    #for a in array:
        #print(a)
###############################   run function
    for c in range(len(array[r])):
        split_em(r,c)


#for a in array:
#    print('')
#    for b in a:
#        print(b,'\t',end='')

for n in array[-1]:
    if isinstance(n,int):
        print(n,end='')
        answer += n

print('')
print('\033[92mAnswer:',answer,'\033[0m')

import os
import copy

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
array = []
array2 = []

def map_out_array(target):
    for a in target:
        print('[', end='')
        for b in a:
            print(b,end='')
        print(']')
    #for r in range(len(target)):
    #     for c in range(len(array[r])):
    #        print('(',r,',',c,') = ',array[r][c])



def whats_surrounding(tgt_map,row,col):
    around = []
    rows = len(tgt_map)
    cols = len(tgt_map[0]) if rows > 0 else 0

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < rows and 0 <= j < cols:
                if (i, j) != (row, col):
                    around.append(tgt_map[i][j])            
    return around


with open(inputfile, 'r') as file:
    for line in file:
        l = list(line.strip())
        array.append(l)

array2 = copy.deepcopy(array)

def do_it():
    rolls_moved = 0
    global array, array2, answer, run
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == '@':
                paper = whats_surrounding(array,r,c)
                rolls = paper.count('@')
                if rolls < 4:
                    array2[r][c] = '.'
                    rolls_moved += 1
    #print(rolls_moved,end='')
    answer = answer + rolls_moved
    if int(rolls_moved) > 0:
        array = copy.deepcopy(array2)
        #print('\n',rolls_moved,'rolls moved')
        #map_out_array(array)
    else:
        run = not run





run = True

while run:
    do_it()


#map_out_array(array2)
print('\033[92m',answer,'\033[0m')


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
        #print(line)
        #line = line.strip()
        line = line.split()
        newline = []
        for l in line:
            newline.append(l)
        input.append(newline)

for i in input:
    print(i)


#print('\n\033[92mAnswer:',area,'\033[0m')
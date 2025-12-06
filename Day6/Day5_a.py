import os

current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\input.txt'

answer = 0
array = []

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()



print('\033[92m',answer,'\033[0m')
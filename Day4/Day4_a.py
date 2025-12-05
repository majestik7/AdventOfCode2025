
import os
import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\in_test.txt'

answer = 0
array = []

with open(inputfile, 'r') as file:
    for line in file:


import os
import numpy as np

n = 99
my_array = np.arange(0, n + 1)
my_array = np.roll(my_array, 50)

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

with open(inputfile, 'r') as file:
    i = 0
    for line in file:
        
        line = line.strip()
        lr = line[0]
        n = int(line[1:])

        if lr == 'L':
            my_array = np.roll(my_array, n)
        elif lr == 'R':
             n = n * -1
             #print(n)
             my_array = np.roll(my_array, n)
        else:
            print("n unknown")

        #print(my_array[0])    
        if my_array[0] == 0:
            i += 1

print('i = ',i)



import os

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
fresh = []
ingredients = []

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()
        if l.count('-') > 0:
            l = l.split('-')
            fresh.append(l)
        elif l == [] or l == '':
            continue
        else:
            ingredients.append(int(l))

#print(fresh)
#print(ingredients)

for i in ingredients:
    for f in fresh:
        if int(f[0]) <= int(i) <= int(f[1]):
            answer += 1
            break


print('\033[92m',answer,'\033[0m')

import os

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
fresh = []
ingredients = []

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()
        #print(str(l))
        if l.count('-') > 0:
            l = l.split('-')
            rng = list(range(int(l[0]),int(l[1])+1))
            fresh = list(set(fresh + rng))
        elif l == [] or l == '':
            continue
        else:
            ingredients.append(int(l))


print(fresh)
print(ingredients)

for i in ingredients:
    if i in fresh:
        answer += 1


print('\033[92m',answer,'\033[0m')
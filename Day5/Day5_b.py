
import os

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
fresh = []

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()
        if l.count('-') > 0:
            l = l.split('-')
            l = [int(item) for item in l]
            fresh.append(l)


def conglobulate(array):
    global changes
    changes = 0
    a = array.pop(0)
    for e in range(len(array)):
        if array[e][0] == (a[1] + 1):
            array[e][0] = a[0]
            return array
        elif a != array[e]:
            if array[e][0] <= a[0] <= array[e][1]:
                if a[1] >= array[e][1]:
                    array[e][1] = a[1]
                    return array
                else:
                    return array
        elif a == array[e]:
            return array
    array.append(a)
    return array

x = 0
tries = (len(fresh)*len(fresh))*3
while x < tries:
    fresh = conglobulate(fresh)
    x += 1

sorted_fresh = sorted(fresh, key=lambda x: x[0])

for s in sorted_fresh:
    answer = answer + ((s[1] - s[0]) + 1)
    print(s[0])
    print(s[1])
    print('--------')


print('\033[92m',answer,'\033[0m')
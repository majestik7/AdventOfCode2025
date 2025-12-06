
import os
import copy

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
fresh = []
test = []
extra = 0

with open(inputfile, 'r') as file:
    for line in file:
        l = line.strip()
        if l.count('-') > 0:
            l = l.split('-')
            l = [int(item) for item in l]
            fresh.append(l)

test = copy.deepcopy(fresh)

def do_it():
    print('\033[92mDOIN IT\033[0m')
    global fresh, test, answer, extra
    print(fresh)
    changes = 0
    for f1 in range(len(fresh)):
        #print(fresh[f1])
        for f2 in range(len(fresh)):
            print('f1',fresh[f1],'f2',fresh[f2])
            if fresh[f2][0] <= fresh[f1][0] <= fresh[f2][1]:
                if fresh[f1][1] > fresh[f2][1]:
                    print('placing',fresh[f1][0],'into',fresh[f2],'by updating f1 to',fresh[f1][1])
                    test[0] = fresh[f1][1]
                    if fresh[f1] == fresh[f2]:
                        print('remove',fresh[f1])
                        test.remove(fresh[f1])
                    changes += 1
                else:
                    print('ignoring',fresh[f1],'because it is within',fresh[f2])
                    if fresh[f1] != fresh[f2]:
                        print('remove',fresh[f1])
                        test.remove(fresh[f1])
                    changes += 1
    if changes == 0:
        extra += 1
    test_unique = []
    for t in test:
        if t not in test_unique:
            test_unique.append(t)
    fresh = copy.deepcopy(test_unique)

while extra < 5:
    do_it()

print('\033[92m',answer,'\033[0m')
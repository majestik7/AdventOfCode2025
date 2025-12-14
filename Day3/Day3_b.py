
import os
import itertools
import itertools
#import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0
delim = ''

numlen = 17
combolen = 12

with open(inputfile, 'r') as file:
    for line in file:
        print('working on',line)
        line = line.strip()
        #work line to shorten to smallest string with at least 12
        x = 0
        y = -13
        beginning = ''
        while len(line) > numlen: 
            y = -13 + len(beginning)
            print('xy',x,y)
            if y < 0: 
                if y >= 0:
                    y = ''
                test = line[x:y]
                print('ll',len(line))
                print('len',len(test),'-',test)
                i = test.find(max(test))
                print('max is',max(test),'at',i)
                beginning = line[:x]
                print('beginning',beginning)
                if beginning != '':
                    if len(beginning) > 12:
                        while len(line) > 15:
                            lst = sorted(list(line))
                            if len(lst) > 0:
                                rm = lst.pop(0)
                                if line.count(rm) > 0:
                                    i = line.index(rm)
                                    line = line[:i]+line[i+1:]
                        break
                i = i + x
                line = line[i:]
                line = beginning + line
                print(line)
                x += 1
            else:
                print('y \033[91m NOT \033[0m] < 0')
        print(line)



        numbers = list(line)
        maxcombo = 0
        all_jolts = []
        all_jolts = list(itertools.combinations(numbers, combolen))
        #print(all_jolts)
        maxjolt = max(all_jolts)
        maxv = int(delim.join(maxjolt))
        print('max','\033[94m',maxv,'\033[0m]')
        answer = answer + maxv
print('\033[92m',answer,'\033[0m]')
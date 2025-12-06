
import os
import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\in_test.txt'

answer = 0

numlen = 12
delim = ''


with open(inputfile, 'r') as file:
    for line in file:
        jolt = []
        line = line.strip()
        print('line',line)
        l = list(line)
        #numlist = list(range(len(l)))
        fullarray = []
        for i in l:
            entry = [i,"off"]
            fullarray.append(entry)
        print('fa',fullarray)
        print('l',l)


        larglist = heapq.nlargest(12,l)
        print('ll1',larglist)

        lastpop = 0


        while sum("on" in tup for tup in fullarray) < 12:
            print(sum("on" in tup for tup in fullarray))
            lp = larglist.pop(0)
            print('take',lp,'ll',larglist)
            for e in reversed(range(len(fullarray))):
                if fullarray[e][1] != "on":
                    if fullarray[e][0] == lp:
                        print('lp',lp,'last',lastpop)
                        print(e, len(fullarray) - 12)
                        fullarray[e][1] = "on"
                        print(fullarray)
                        if int(lp) > int(lastpop):
                            lastpop = lp
                        break
        print('**',fullarray)
        finalnum = []
        for n in range(len(fullarray)):
            if fullarray[n][1] == "on":
                finalnum.append(fullarray[n][0])

        print('\033[91m',finalnum,'\033[0m')









        #answer = answer + int(jolt)
        


print(answer)
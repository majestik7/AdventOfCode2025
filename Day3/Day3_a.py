
import os
import heapq

current_script_dir = os.path.dirname(os.path.realpath(__file__))

inputfile=current_script_dir + '\input.txt'

answer = 0

numlen = 2
delim = ''

def get_largest_index(list, string):
    #print(list, string)
    for s in range(len(list) - 1, -1, -1):
        if list[s] == string:
            return s
    return -1

def get_largest_num(list):
    return heapq.nlargest(1, list)
    

with open(inputfile, 'r') as file:
    for line in file:
        jolt = []
        line = line.strip()
        #print(line)
        l = list(line)
        h = heapq.nlargest(2,l)
        #print('l2',h)
        if len(set(h)) == 1:
            for n in range(0,numlen):
                j = h.pop()
                #print('j',j)
                jolt.append(j)
        else:    
            largest = get_largest_num(l)
            jolt = largest
            if len(jolt) < numlen:
                #print('largest',largest)
                largind = get_largest_index(l, largest[0])
                #print('largind',largind,'lenl',len(l)-1)
                if largind < len(l)-1:
                    l = l[largind+1:]
                    #print('l',l)
                    xstr = get_largest_num(l)[0]
                    jolt.append(str(xstr))
                else:
                    l = l[:largind]
                    #print('l',l)
                    xstr = get_largest_num(l)[0]
                    jolt.insert(0,str(xstr))

        jolt = str(delim.join(jolt))
        #print('jolt',jolt,'\n')

        answer = answer + int(jolt)
        


print(answer)
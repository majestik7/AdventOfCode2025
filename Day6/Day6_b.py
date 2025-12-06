import os
import operator

current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\input.txt'

answer = 0
input = []
temp1 = []
array = []
delim = ''

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

with open(inputfile, 'r') as file:
    for line in file:
        line = list(line[:-1])
        #print(line)
        input.append(line)

nums = []
for d in reversed(range(len(input[0]))):
    digit = ''
    nums = []
    for n in range(len(input)-1):
        digit = digit + input[n][d] 
    nums.append(digit.strip())
    temp1.extend(nums)
    if (nums[0] == ''):
        array.append(temp1[:-1])
        temp1 = []
    le = []
    le.append(int(n))
    le.append(len(input)-2)
    if d == 0 and n == (len(input)-2):
        array.append(temp1[:])
        temp1 = []
o = delim.join(input[-1])
o = o.split()
o = o[::-1]

for p in range(len(o)):
    array[p].append(o[p])

for a in array:
    x = len(a) - 2
    result = 0

    op_char = str(a[x+1][0])
    if op_char == '*':
        result = 1
    elif op_char == '+':
        result = 0
    for n in a[:-1]:
        op_func = ops[op_char]
        result = op_func(int(result), int(n))
    answer = answer + result


print('\033[92m',answer,'\033[0m')
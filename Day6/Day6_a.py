import os
import operator


current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\input.txt'

answer = 0
array = []
input = []
delim = ''

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,  # Use truediv for float division
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow
}



with open(inputfile, 'r') as file:
    for line in file:
        line = line.strip().split()
        input.append(line)


for i in range(len(input[0])):
    problem = []
    for e in range(len(input)):
        l = []
        l.append(input[e][i])
        problem.append(l[0])    
    array.append(problem)

print(array)

for a in array:
    x = len(a) - 2
    result = 0

    op_char = str(a[x+1][0])
    if op_char == '*':
        result = 1
    elif op_char == '+':
        result = 0
    print(op_char)
    for n in a[:-1]:
        print(str(n))
        op_func = ops[op_char]
        result = op_func(int(result), int(n))
    print(result)
    answer = answer + result


print('\033[92m',answer,'\033[0m')
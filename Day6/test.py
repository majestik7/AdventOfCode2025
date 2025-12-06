import operator

# Create a dictionary mapping operator symbols to their corresponding functions
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,  # Use truediv for float division
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow
}

a = 10
b = 5

# Get the operator symbol from user input or a predefined value
op_char = "+"  # Example: user wants to add
# op_char = input("Enter an operator (+, -, *, /): ")

# Retrieve the corresponding function from the dictionary
op_func = ops[op_char]

# Use the function to perform the operation
result = op_func(a, b)
test = f'{a} {op_char} {b} = {result}'
print(f"{test}")

op_char = "*"
op_func = ops[op_char]
result = op_func(a, b)
print(f"{a} {op_char} {b} = {result}")
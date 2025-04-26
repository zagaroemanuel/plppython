print("Enter first number:")
a = float(input())    # Input first number   
print("Enter second number:")
b = float(input())   # Input second number
print("Enter operator (+, -, *, /):")
op = input()   # Input operator 

# Perform the operation based on the operator
if op == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif op == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif op == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif op == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")


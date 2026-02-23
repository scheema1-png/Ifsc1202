frist = float(input("Enter the frist number: "))
op = input("Enter the operator (+, -, *, /): ")
second = float(input("Enter the second number: "))
if op == "+":
    print(frist, "+", second, "=", frist + second)
elif op == "-":
    print(frist, "-", second, "=", frist - second)
elif op == "*":
    print(frist, "*", second, "=", frist * second)
elif op == "/":
    print(frist, "/", second, "=", frist / second)
else:
    print("Invalid operator")
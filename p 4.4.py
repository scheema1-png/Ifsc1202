numzeroes = 0
n = int(input("Enter a number: "))
for i in range(n):
    num = int(input("Enter number: ")) 
    if num == 0:
        numzeroes += 1
print(f"Number of zeroes: {numzeroes}")
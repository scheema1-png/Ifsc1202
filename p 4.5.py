n = int(input("Enter Number: "))
partialfactorial = 1
partialsum = 0
for i in range(1, n + 1):
    partialfactorial = 1
    partialfactorial *= i
    partialsum += partialfactorial
    print("Sum of factorials:{}". format (partialsum))
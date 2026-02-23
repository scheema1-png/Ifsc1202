start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers between", start, "and", end)
for num in range(start, end + 1):
    temp = num
    count = 0
    while temp > 0:
        temp //= 10
        count += 1
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
    if total == num:
        print(num)

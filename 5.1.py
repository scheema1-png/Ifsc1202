sequencesum = 0
value = input("Enter a number(cr to stop): ")
while value != "":
    sequencesum += int(value)
    value = input("Enter a number(cr to stop): ")
print("The sum of the sequence is: ", sequencesum)
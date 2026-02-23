sequencesum = 0
sequencecount = 0
value = input("Enter a number(cr to stop): ")
while value != "":
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a number(cr to stop): ")
if sequencecount > 0:
    print("The sum of the sequence is: ", sequencesum)
    print("The average of the sequence is: ", sequencesum / sequencecount)
else:
    print("No numbers were entered.")
    
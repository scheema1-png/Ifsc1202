value = input("Enter a number(cr to stop): ")
if value == "":
    maximum = int(value)
    while value != "":
        if int(value) > maximum:
            maximum = int(value)
        value = input("Enter a number(cr to stop): ")
    print("The maximum is", maximum)
else:
    print("sequence length is zero")


value = input("Enter a number(cr to stop): ")
if value == "":
    maximum = int(value)
    maximumindex = 1
    currentindex = 1
    while value != "":
        if int(value) > maximum:
            maximum = int(value)
            maximumindex = currentindex
        value = input("Enter a number(cr to stop): ")
        currentindex += 1
    print("The maximum is", maximum, "at index", maximumindex)
else:
    print("sequence length is zero")
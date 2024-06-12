mainString = "banana"
inp = input("What ministring would you like to find within the main string? ")
count = 0

if (len(inp)<len(mainString)):
    for x in range (0, len(mainString)-len(inp)):
        temp = mainString[x: x+len(inp)]
        if (temp == inp):
            count +=1
    print("Your ministring appeared in the main string " + str(count) + " times.")
else:
    print("Your input was too large of a string to be found in the main string!")

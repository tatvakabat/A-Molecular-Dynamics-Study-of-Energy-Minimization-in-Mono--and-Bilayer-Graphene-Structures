inp = input("Enter a file name: ")
try:
    fhand = open(inp)
except:
    print("File name " + inp + " not found")
    quit()

for line in fhand:
    print(line.upper())

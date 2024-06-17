inpFile = input("Enter the name of the file you would like to read: ")
file = open(inpFile)
msgsToBeRead = []

for line in file:
    line.rstrip()
    words = line.split()
    if (words[0] != "From"):
        continue
    msgsToBeRead.append(line)

print("All messages to be read are:")
print(msgsToBeRead)

# Simple program to detect the number of unique words & their frequency in a .txt file

fname = input('Enter a file name: ')

try:
    file = open(fname)
except:
    print("File not found")
    quit()

wordList = dict()

for line in file:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        wordList[word] = wordList.get(word,0) + 1

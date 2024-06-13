count = 0
sum = 0.0

while True:
    inp = input("Enter a number: ")
    if (inp == "done"):
        break
    count+=1
    sum+=float(inp)

print("Total: ", sum)
print("Counter: ", count)
print("Average: ", (sum/count))

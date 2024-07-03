from matplotlib import pyplot as plt

values = []
indexes = []
count = 0

while True:
    x = input("Enter a value for the pie chart in form name,value and type done when finished: ")
    if x.lower() == "done":
        break
    try:
        name, value = x.split(",")
        value = float(value.strip())
        indexes.append(name.strip())
        values.append(value)
        count +=1
    except ValueError:
        print("Invalid format. Please enter in form name,value")

plt.pie(values, labels = indexes, shadow = True)
plt.title("Generated Pie Plot")
plt.tight_layout()
plt.show()

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try: 
    hours = float(hours)
    rate = float(rate)
except:
    print("Please enter a numerical input")
    quit()

if (hours > 40):
    print("Overtime")
    othours = hours-40
    hours = 40
else:
    print("Regular")
    othours = 0

print("Pay: ", (hours*rate + othours*rate*1.5))
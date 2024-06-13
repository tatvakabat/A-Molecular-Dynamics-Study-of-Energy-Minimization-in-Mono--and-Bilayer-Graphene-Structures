def calculateGrossPay(hours, rate):
    return(hours*rate)

nHours = (float) (input("Enter number of hours: "))
nRate = (float) (input("Enter your rate: "))

print("Total Pay: ", calculateGrossPay(nHours,nRate))
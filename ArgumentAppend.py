digitsString = input("Цілі числа розділені комою: ")
digitStringList = digitsString.split(" ")
xDigitStringList = list()

for i in range(0, len(digitStringList)):
    xDigitStringList.append("x=" + digitStringList[i])
    
completeString = ""
for s in xDigitStringList:
    completeString += (s + ", ")
    
print(completeString)
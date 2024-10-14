stirng1 = input("Рядок 1: ")
string2 = input("Рядок 2: ")

cList1 = list()
for c in stirng1:
    if not c in cList1:
        cList1.append(c)

for c in string2:
    if c in cList1:
        cList1.remove(c)
    
print("У другому рядку в порівнянні з першим бракує: ", cList1)

aList = [1, 4, 9, 16, 25]
evens = [el * 1 for el in aList if el % 2 == 0]
odds = [el for el in aList if el % 2 == 1]
#print(evens)
print(odds)
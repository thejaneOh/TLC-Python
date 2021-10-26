valOne = 0
valTwo= 1
store = 2

print(valOne)
print(valTwo)

while(store!=20):
    toPrint = valOne + valTwo
    valOne = valTwo
    valTwo=toPrint
    print(toPrint)
    store+=1


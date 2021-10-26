#-------------playing with functions

def inc(x):
    x=x+1


x=10
inc(x)
#print(x)

def f1(list1):
    list1.append("!!!")



l=['a','b']



#__________________Question 2_____________________________________

def lastToFirst(theList):
    #get last value
    last = theList.pop()
    #put it infront
    theList.insert(0,last)
    #adding to the end is appending

hey = ['a','b','c','d','e']
lastToFirst(hey)
print(hey)

me = [1,3]


#__________________Question 3_____________________________________
def getValue(theList,indiceList):
    newList = []
    for a in indiceList:
        newList.append(theList[a])
    return newList 


print(getValue(hey,me))


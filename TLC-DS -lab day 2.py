#Create a regular Python array of 1000 integers -
import timeit
import time
anArray = range(1000)
arrPow2 = [x**2 for x in anArray]
#print(arrPow2)



print(timeit.timeit(stmt='[x**2 for x in myArray]',setup ='myArray = range(1000)', number =1000))

print(timeit.timeit(setup='import numpy as np;otherArray = np.arange(1000)',stmt='[x**2 for x in otherArray]', number=1000))

#statement, steup, timer,number,gloabls

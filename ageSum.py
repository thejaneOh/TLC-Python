age= int(input("Please enter your age: "))

newSum =0
#ageY = age
while(age!=0):
    newSum+= age
    age-=1


print("the sum of all years your age is " + str(newSum))
forMonths = newSum*12
print("Your age in months is "+ str(forMonths))
forDays = newSum*365
print("Your age in days is "+ str(forDays))
forHours = newSum*365*24
print("Your age in hours is "+ str(forHours))



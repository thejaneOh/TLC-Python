import random

random.Random()
# selects a value between 0.0 and 1.0
myNum= random.randint(1,10)
print(myNum)

aguess = int(input("Hello. I am thinking of a number between 1 and 10. Can you try guessing it? "))
if myNum == aguess:
    print("You are a genius!!! The number is indeed: ", aguess)
else:
    print("Sorry, that is not the number.")
    while (myNum != aguess):
        aguess = int(input("Please try again: "))
        if myNum == aguess:
            print("Great!!!!, The number is indeed: " , aguess)
            break
        else:
            print("Sorry, that is not the number.")


#random.randint(100,200)      # integers between 100 and 200
#random.randrange(100,200,2)  # even numbers between 100 and 200

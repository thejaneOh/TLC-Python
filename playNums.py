playStore = []
print("Please enter a number between 1 and 8 after each prompt")
for n in range(10):
    playStore.append(int(input("Please enter a number: ")))

num5 = playStore.count(5)

print(num5)
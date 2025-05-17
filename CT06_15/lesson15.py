# print("Hello from lesson 14")
counter=0

def increase():
    global counter 
    counter +=1
for i in range(3):
    increase()
    i
print(counter)
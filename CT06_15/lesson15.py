# print("Hello from lesson 14")
counter=0

def increase(num):
    global counter 
    counter +=1
for i in range(3):
    increase(1)
    
print(counter)
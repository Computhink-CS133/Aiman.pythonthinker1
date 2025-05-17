# # print("Hello from lesson 14")
# counter=0

# def increase(num):
#     global counter 
#     counter +=num
# for i in range(3):
#     increase(1)
    
# print(counter)

def isEven(num):
    return num % 2 == 0



for i in range(1,101):
    if isEven(i):
        print(str(i)+ " is even")
    else:
        print(str(i)+" is odd")
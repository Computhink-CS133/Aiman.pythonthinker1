# # print("Hello from lesson 14")
# counter=0

# def increase(num):
#     global counter 
#     counter +=num
# for i in range(3):
#     increase(1)
    
# print(counter)

# def isEven(num):
#     return num % 2 == 0



# for i in range(1,101):
    # if isEven(i):
    #     print(str(i)+ " is even")
    # # else:
    #     print(str(i)+" is odd")

import random

def square(num):
    return num*num
print(square(random.random()))

def sum_squae(num1,num2):
    return num1*num2+num2*num2
print(sum_squae(182635,1038103))
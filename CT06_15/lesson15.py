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

import random as r

def square(num):
    return num*num
# print(square(random.random()))


def sum_squae(num1,num2):
    return square(num1) + square(num2)
input1=str(r.randint(1,100))
input2=str(r.randint(1,100))
print(input1 +" squared "+ "+"input2 + " squared" + "=" str(sum_squae(input1,input2)))
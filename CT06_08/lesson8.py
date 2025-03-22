# print("Hello from lesson 8")

# import time

# secs=int(input("What is the number of seconds you want to count down? "))

# for i in range(secs,0,-1):
#     print(i)
#     time.sleep(1)

# print("Time's up!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# print("!!!!!!!!!!!!!!!!!!!!"
# "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 

# import random
# # print(random.randint(1,6))
# print("Your 20 lucky numbers are")
# for i in range(20):

#     print(random.randint(0,9999))
# print("Congrats!")

# var1=True
# var2=False



# print(var1==var2)

# import random



# rounds=int(input("How many questions do you want? "))


# for i in range(rounds):
#     num1=random.randint(1,50)
#     num2=random.randint(1,50)   
#     ans=int(input("What is "+ str(num1)+"+"+str(num2)+"? "))
#     if (ans==num1+num2):
#         print("Correct")
#     else:
#         print("Wrong. Answer is "+str(num1+num2))

import random as r

# rounds=int(input("How many questions do you want? "))

# for i in range(rounds):
#     num1=r.randint(1,10)
#     num2=r.randint(1,10)
#     Ans=int(input("What is "+str(num1)+" x "+str(num2)+"? "))
#     print("Your answer is "+ str(Ans==num1*num2))
#     print("The answer is "+str(num1*num2))

num1=r.randint(1,6)
num2=r.randint(1,6)
num3=r.randint(1,6)
alleven=num1 % 2==0 and num2 % 2==0 and num3 % 2==0
allodd=num1 % 2==1 and num2 % 2==1 and num3 % 2==1

print("Number 1: "+str(num1) )
print("Number 2: "+str(num2) )
print("Number 3: "+str(num3) )
print("All numbers are even: "+str(alleven))
print("All numbers are odd: "+str(allodd))
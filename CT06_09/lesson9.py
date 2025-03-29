# # # print("Hello from lesson 9")

# # import random as r

# # num1=r.randint(1,6)
# # num2=r.randint(1,6)
# # num3=r.randint(1,6)
# # alleven=num1 % 2==0 and num2 % 2==0 and num3 % 2==0
# # allodd=num1 % 2==1 and num2 % 2==1 and num3 % 2==1

# # print("Number 1: "+str(num1) )
# # print("Number 2: "+str(num2) )
# # print("Number 3: "+str(num3) )
# # print("All numbers are even: "+str(alleven))
# # print("All numbers are odd: "+str(allodd))

# # DAYS=int(input("How many days have you been borrowing the book? "))

# # if DAYS>25:
# #     print("Remember to return it.")



# # import random as r

# # num=r.randint(1,10)
# # ans=int(input("Guess the number "))
# # if num==ans:
#     # print("Hooray")






# numapples=int(input("How many apples do you want? "))
# numoranges=int(input("How many oranges do you want? "))

# appleprice=0.60*numapples
# if numapples>5:
#     appleprice=(appleprice-(appleprice/10))

# orangeprice=0.90*numoranges
# if numoranges>5:
#     orangeprice=(orangeprice-(orangeprice/10))

# print(appleprice+
# days=int(input("How many days are there? "))
# hotdays=0

# for i in range(days):
#     temp=int(input("What is the temperature? "))
#     if temp>30:
#         hotdays+=1


# print("There are "+str(hotdays)+" hot days. ")
























desire=0
undesire=0
for i in range(10):
    rate=int(input("Please leave a rating. "))
    if rate>3:
        desire+=1
    else:
        undesire+=1

if undesire>desire:
    print("")
# money=1000
# amount=0
# while True: 
#     print("Choose a choice number")
#     print("1.Withdraw")
#     print("2.Deposit")
#     print("3.Check money")
#     print("4.Get out")
#     choice=int(input("Choose one "))
#     if choice==1:
#         amount==int(input("How much money you want to withdraw "))
#         if amount<=money:
#             money-=amount
#             print("You have "+ str(money)+" moneys")
#         else:
#             print("An error occured!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     if choice==2:
#         amount==int(input("How much to deposit "))
#         money+=amount
#         print("You have "+ str(money)+" moneys")
#     if choice==3:
#         print("You have "+ str(money)+" moneys")
#     if choice==4:
#         break
# print("You have "+ str(money)+" moneys")

toppings=[
    "1. Pepperoni",
    "2. Cheese",
    "3. Lettuce",
    "4. Tomato",
]

print("You can add "+ str(toppings) +" toppings" )


# create list of pizza toppings

# print out the toppings in a menu for the user

user_toppings=[]

while True:
    add=input("What number of the topping to add. Type end to end ")
    if add== "end":
        break
    else:

        user_toppings.append(toppings[int(add)-1])

for i in range(len(user_toppings)):
    print(user_toppings[i])









































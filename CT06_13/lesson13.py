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

user_toppings=[]


while True:
    add=input("What number of the topping to add. Type end or type text to end ")
    if add== "end" or type(add)==str:
        break
    else:

        user_toppings.append(toppings[int(add)-1])


print("You ordered:")
if len(user_toppings)>=1:
    for i in range(len(user_toppings)):
        print(user_toppings[i])
    else:
        print("NOTHING :)")









































money=1000
while True: 
    print("Choose a choice number")
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check money")
    print("4.Get out")
    choice=int(input("Choose one"))
    if choice==1:
        amount=int(input("How much money you want to deposit"))
        if amount<=money:
            money-=amount
            print("You have")

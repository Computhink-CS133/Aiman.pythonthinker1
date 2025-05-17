# # print("Hello from lesson 14")
# counter=0

# def increase(num):
#     global counter 
#     counter +=num
# for i in range(3):
#     increase(1)
    
# print(counter)

def EvenOrOdd(num):
    global number
    number+=1
    return num % 2 ==0


number=0
for i in range(100):
    result=EvenOrOdd(number)
    if result:
        print(str(number)+ " is even")
    else:
        print(str(number)+" is odd")
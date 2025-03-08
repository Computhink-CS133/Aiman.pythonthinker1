Start=int(input("What number do you want to start with "))#ask for start number and converts start number to integer
Stop=int(input("What number do you want to stop with "))#ask for stop number and converts stop number to integer
step=int(input("What is the increament "))#ask for increament and converts increament to integer


for i in range(Start,Stop,step):
    print(i)


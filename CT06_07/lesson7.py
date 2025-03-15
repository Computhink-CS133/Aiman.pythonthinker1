# # # # print("Hello from lesson 7")


# # # # Lesson 7 - For Loop (Part 2)

# # # ## Recap 1: Debugging Average Score Program

# # # ### There is a total of 3 bugs in the following program.
# # # ### Identify and fix the bugs:

# # # score_one = 80
# # # score_two = 90
# # # score_three = 75

# # # total = score_one + score_two + score_three

# # # average_score = total / 3

# # # student_name = "Alex"

# # # print("Average score for " + student_name + " is: " + str(round(average_score,2)))

# # for i in range(1,11):
# #     print(i) #Prints out i variable

# # for i in range(2,21,2):
# #     print(i) #Prints out i variable

# # for i in range(10,0,-1):
# #     print(i) #Prints out i variable

# # word=input("Whatttttt isssss urrrrrrr nameeeeeee????????  ")

# # rep=input("Oooookay! How many names of that name do you want? Write a value. ")

# # for i in range(int(rep)):
# #     print("Hello thereee "+word)



# sum=0

# for i in range(1,6):
#     sum=sum+int(input("What is number "+str(i)+"?"))

# print(sum)















# num=input("What is da number for da time table???????")

# number=input("How long is da time table?")

# for i in range(1,int(number)+1):
#     print(num+"X"+ str(i)+"="+str(int(num)*i))






# num=int(input("Give me a number "))

# for i in range(1,num+1):
#     print(str(i)*i)

total=0
for i in range(5):
    total=total+input("What is the score of this students")
# print("Hello from lesson 6")

students=int(input("How many students are there?"))

score=0

for i in range(students):
    score=score+int(input("The score of this student? "))

Average=score/students

print("The average is")
print(round(Average))


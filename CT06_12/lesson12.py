

# visitors=4
# while visitors<25:
#     visitors+=1
#     print(visitors)

# max_pax=30
# pax=0
# while True:
#     add_pax=input("Add a visitor?")
#     if add_pax=="yes":
#         pax+=1
#     if pax>max_pax:
#         break





order=""
while True:
    want=input("Order some food. ")
    if want=="end":
        break
    order+=order+", " 

order=str(order)-", " 
print(order) 


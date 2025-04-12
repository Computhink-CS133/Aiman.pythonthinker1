

# visitors=4
# while visitors<25:
#     visitors+=1
#     print(visitors)

max_pax=30
pax=0
while True:
    add_pax=input("Add a visitor?")
    if add_pax=="yes":
        pax+=1
    if pax>30:
        break


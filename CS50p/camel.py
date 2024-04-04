name=input("camelCase: ")
alphabet=["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y","Z"]


for c in name:
    if c in alphabet:
        lilc=c.lower()
        print("_"+lilc,end="")
    else:
        print(c, end="")
print()





#TODO : need to split str name at capital letters]

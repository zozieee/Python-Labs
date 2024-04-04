import sys
due=50

while due>0:
    print(f"Amount Due: {due}")
    amt=int(input("Insert coin: "))
    if  amt ==int(5):
        due-=5
    elif amt ==int(10):
        due-=10
    elif amt ==int(25):
        due-=25
    #else:
       # print("Invalid denomination: must be 5, 10, or 25 cents")

while due<=0:
    sys.exit(f"Change Owed: {abs(due)}")
    #  amt=int(input("Insert coin: "))
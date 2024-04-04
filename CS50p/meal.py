#b=7-8am
#l=12-13
#d=18-19

def main():
    time=input("What time is it? ")
    con=convert(time)
    if 7.00<=con<= 8.00: print("breakfast time")

    elif 12.00 <= con <= 13.00: print("lunch time")
    elif 18.00 <= con<= 19.00: print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    con=0.00

    mm=float(minutes)/60
    con+=float(hours)+mm
    return con

if __name__=="__main__":
    main()
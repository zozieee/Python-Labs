months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    input=input("Date: ")
    date=input.strip()
    try:
        mm,dd,yyyy=date.split("/",3)
        if ((1<=int(mm)<=13) and (1<=int(dd)<=31)):
            print(f"{yyyy}-{int(mm):02}-{int(dd):02}")
            break
    except:
        try:
            mm,dd,yyyy=date.split(" ",3)

            for i in range(len(months)):
                if mm.capitalize()==months[i]:
                    month=i+1
            day=dd.replace(",","")
            if ((1<=int(month)<=13) and (1<=int(day)<=31)):
                print(f"{yyyy}-{int(month):02}-{int(day):02}")
                break
        except:
            pass



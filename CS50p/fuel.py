def main():
    fuel=input("Fraction: ")
    dividend, divisor = fuel.split("/")

    while dividend.isnumeric() == False or divisor.isnumeric() == False:
        fuel=input("Fraction: ")
        dividend, divisor = fuel.split("/")

    if dividend.isnumeric() == True and divisor.isnumeric() == True:
        if int(dividend) <= int(divisor):
            percent=int(dividend) / int(divisor)

            if percent <= .01:
                print("E")
            elif percent >= .99:
                print("F")
            else:
                result=int(percent * 100)
                print(str(result)+"%")
        elif divisor==0:
            raise ZeroDivisionError
        else:
            raise ValueError

try:
    main()
except ZeroDivisionError:
    main()
except ValueError:
    main()






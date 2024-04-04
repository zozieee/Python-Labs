exp=input("Expression: ")
split= exp.split(" ", 2)



x=float(split[0])
y=split[1]
z=float(split[2])

match y:
    case "+":
        ans=x+z
        print(f"{ans:.1f}")
    case "-":
        ans=x-z
        print(f"{ans:.1f}")
    case "*":
        ans=x*z
        print(f"{ans:.1f}")
    case "/":
        ans=x/z
        print(f"{ans:.1f}")


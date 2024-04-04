def main():
    greet=input("Greeting: ")
    greet=greet.strip()
    greet=greet.lower()

    if "hello" in greet:
        print("$0")
    elif greet[0]=="h":
        print("$20")
    else:
        print("$100")

main()
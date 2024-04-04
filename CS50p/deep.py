def main():
    ans=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    ans=ans.strip()
    lower=ans.lower()

    if lower=="42":
        print("Yes")
    elif lower=="forty-two":
        print("Yes")
    elif lower=="forty two":
        print("Yes")
    else:
        print("No")

main()

def main():
    reply=input("Convert your emoticon to an emoji here: ")
    print(convert(reply))


def convert(emote):
    conv1=emote.replace(":)", "🙂")
    conv2=conv1.replace(":(", "🙁")
    return conv2
main()

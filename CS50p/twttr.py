def main():
    tweet=input("Input: ")



    print("Output: "+ removeUpper(removeLower(tweet)))



def removeLower(tweet):
    twta=tweet.replace("a","")
    twte=twta.replace("e","")
    twti=twte.replace("i","")
    twto=twti.replace("o","")
    twtu=twto.replace("u","")
    return twtu
def removeUpper(twtu):
    twt1=twtu.replace("A","")
    twt2=twt1.replace("E","")
    twt3=twt2.replace("I","")
    twt4=twt3.replace("O","")
    final=twt4.replace("U","")
    return final

main()

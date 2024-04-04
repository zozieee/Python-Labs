dict={

}
while True:
     #accept input until ctrl-d
    try:
            item = input().upper()
            if item in dict:
                dict[item]+=1
            else:
                 dict[item]=1

    except EOFError:
        #list items
        print("")
        for key in sorted(dict.keys()):
             print(dict[key],key)
        break
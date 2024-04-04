import emoji
string=input("Input: ")
estring=emoji.emojize(string)
emostring=emoji.emojize(estring, language='alias')

print(emostring)





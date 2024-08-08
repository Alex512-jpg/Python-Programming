CLEAR = "\033c"

porp = ''
data1 = ''
data1 = input(CLEAR + "\nType in the data you want to store\n\n")

while porp != "yes":
    print(CLEAR + "\nDo you want to retrieve your data?\n")
    print("[Yes]")
    porp = input("[No]\n\n").lower().strip()

    if porp == "yes":
        print(CLEAR)
        print("Your inserted data:\n\n" + data1)
    else:
        thirdo = ''
        thirdo = input(CLEAR + "\nAre you sure you don't want to retrieve your data?\n\n[Yes]\n[No]\n\n")
        if thirdo == "no":
            pass
        else:
            break
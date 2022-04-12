s = "zero zero three double four triple one seven zero"

a = s.split()
b =[]
for i in range(len(a)):
    if a[i] == "zero":
        b.append("0")
    elif a[i] == "one":
        b.append("1")
    elif a[i] == "two":
        b.append("2")
    elif a[i] == "three":
        b.append("3")
    elif a[i] == "four":
        b.append("4")
    elif a[i] == "five":
        b.append("5")
    elif a[i] == "six":
        b.append("6")
    elif a[i] == "seven":
        b.append("7")
    elif a[i] == "eight":
        b.append("8")
    elif a[i] == "nine":
        b.append("9")
    elif a[i] == "double":
        if a[i+1] == "zero":
            b.append("0")
        elif a[i+1] == "one":
            b.append("1")
        elif a[i+1] == "two":
            b.append("2")
        elif a[i+1] == "three":
            b.append("3")
        elif a[i+1] == "four":
            b.append("4")
        elif a[i+1] == "five":
            b.append("5")
        elif a[i+1] == "six":
            b.append("6")
        elif a[i+1] == "seven":
            b.append("7")
        elif a[i+1] == "eight":
            b.append("8")
        elif a[i+1] == "nine":
            b.append("9")
    elif a[i] == "triple":
        if a[i+1] == "zero":
            b.append("0")
            b.append("0")
        elif a[i+1] == "one":
            b.append("1")
            b.append("1")
        elif a[i+1] == "two":
            b.append("2")
            b.append("2")
        elif a[i+1] == "three":
            b.append("3")
            b.append("3")
        elif a[i+1] == "four":
            b.append("4")
            b.append("4")
        elif a[i+1] == "five":
            b.append("5")
            b.append("5")
        elif a[i+1] == "six":
            b.append("6")
            b.append("6")
        elif a[i+1] == "seven":
            b.append("7")
            b.append("7")
        elif a[i+1] == "eight":
            b.append("8")
            b.append("8")
        elif a[i+1] == "nine":
            b.append("9")

c = "".join(b)
print(c)
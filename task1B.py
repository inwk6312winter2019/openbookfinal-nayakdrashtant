# Task 1B
import string

def removepunct(word=""):
    punc = string.punctuation
    for p in punc: 
        word = word.replace(p,"")
    return word

def list_unique(Book):
    new_list = []
    fp = open(Book,"r")
    for f in fp:
        f = f.strip()
        f = f.split()
        if len(f) != 0:
            for s in f:
                s = removepunct(s)
                if s not in new_list:
                    new_list.append(s)
    return new_list

def custom_function():
    check = []
    check2 = []
    book1 = list_unique("Book1.txt")
    book2 = list_unique("Book2.txt")
    book3 = list_unique("Book3.txt")
    for bo1 in book1:
        for bo2 in book2: 
            if (bo2 == bo1):
                if bo2 not in check:
                    check.append(bo2)

    for bo3 in book3:
        for che in check:
            if (che == bo3):
                if che not in check2:
                    check2.append(che)

    toptw = check2[0:20]
    count = 0
    mydict = dict()
    for ch in toptw:
        mydict[ch] = count
        count += 1
    print(mydict)


custom_function()

# Drashtant Nayak

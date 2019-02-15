# Task 1 Sub Task 2

def isinthis(word):
    checklist = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    flag = False
    for chk in checklist:
        if word == chk:
            flag = True
        else:
            flag = False
    return flag   

def unique_words(book):
    mylist = []
    f = open(book,"r")
    for re in f:
        re = re.strip()
        re = re.split()
        for r in re:
            if r != "":
                if r not in mylist:
              #  re = re.strip()
                    mylist.append(r)
    
    return mylist

def count_the_article(Book):
    list = unique_words(Book)
    mydict = dict()
    for li in list:
        check = isinthis(li)
        if check == True:
            if li not in mydict:
                mydict[li] = 1
            else:
                mydict[li] += 1
    return mydict

var = input("enter name of book:")
print("Output is:",count_the_article(var))


# Drashtant Nayak

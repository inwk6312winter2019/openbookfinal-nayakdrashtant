from collections import OrderedDict
import operator
## Task 1 Sub task 4
def character_word_count(Book):
    mylist = dict()
    fopen = open(Book,"r")
    for re in fopen:
        re = re.strip()
        re = re.split()
        for r in re:
            if r not in mylist:
                mylist[r] = len(r)
    return mylist

var = input("Enter book name:")
print("Output is:", character_word_count(var))
print("character word counts are stated above")

# Drashtant Nayak

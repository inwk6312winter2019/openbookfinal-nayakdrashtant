from collections import OrderedDict
import operator
## Task 1 Sub task 3
def sorted_words(Book):
    mylist = dict()
    fopen = open(Book,"r")
    for re in fopen:
        re = re.strip()
        re = re.split()
        for r in re:
            if r not in mylist:
                mylist[r] = len(r)
  #  d_descending = OrderedDict(sorted(mylist.items(),key=lambda kv: kv[1]['key3'], reverse=True))
#    sorted_d = sorted(mylist.items(), key=operator.itemgetter(0)) 
    sorted_x = sorted(mylist.items(), key=operator.itemgetter(1), reverse = True)
    return sorted_x

var = input("Enter book name:")
print("Output is:", sorted_words(var))


# Drashtant Nayak

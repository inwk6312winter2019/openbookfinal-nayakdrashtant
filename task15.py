# Sub task 5 of Task 1
mydict = dict()
def histgram(Book):
    fopen = open(Book,"r")
    for re in fopen:
        re = re.strip()
        re = re.split()
        if len(re) != 0:
            for r in re:
                r = r.lower()
                if r[:1] == 'a' or r[:1] == 'e' or r[:1] == 'i' or r[:1] == 'o' or r[:1] == 'u': 
                    if r not in mydict:
                         mydict[r] = 1
                    else: 
                         mydict[r] += 1
    return mydict

def starts_with_vow():
    booklist = ["Book1.txt","Book2.txt","Book3.txt"]
    for book in booklist:
        histgram(book)
    return mydict

#var = input("Enter name of book:")
print("output:",starts_with_vow())


# Drashtant Nayak

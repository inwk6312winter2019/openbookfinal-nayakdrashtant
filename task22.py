import operator
# task 2 subtask 2 
def toptipaddr():
    mydict = dict()
    fopen = open("access.log","r")
    for fop in fopen:
        if "GET /" in fop or "POST /" in fop:
            ip = fop.split('-')[0]
            if ip not in mydict:
                mydict[ip] = 1
            else:
                mydict[ip] += 1
    orted_x = sorted(mydict, key=mydict.get, reverse=True)[:20]
    return orted_x


print(toptipaddr())
# Drashtant Nayak

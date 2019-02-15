# Task 2 subtask 1
def writelogs():
    fopen = open("access.log","r")
    fget = open("get.log","w")
    fpost = open("post.log","w")
    fput = open("put.log","w")
    fdelete = open("delete.log","w")
    for fpe in fopen:
        if "GET /" in fpe:
            fget.write(fpe)
        elif "POST /" in fpe:
            fpost.write(fpe)
        elif "PUT /" in fpe:
            fput.write(fpe)
        else:
            fdelete.write(fpe)


writelogs()


# Drashtant Nayak

# task 2 subtask 3
def getcount():
    fopen = open("access.log","r")
    firefox = []
    chrome = []
    other = []
    for fop in fopen:
        if "Firefox/" in fop:
            firefox.append(fop)
        elif "Chrome/" in fop:
            chrome.append(fop)
        else: 
            other.append(fop)
    print("No of request per browser are as follows:")
    print("Firefox",len(firefox))
    print("Chrome",len(chrome))
    print("Other",len(other))

getcount()

# Drashtant Nayak

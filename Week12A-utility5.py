# Blake Partis
# CSCI 102 - Section B
# Week 12A

def PrintOutput(string):
    print("OUTPUT", string)
    
def LoadFile(file):
    my_list = []
    f = open(file, "r")
    for line in f:
        line = line.strip("\n")
        my_list.append(line)
    f.close
    print("OUTPUT", my_list)

def UpdateString(string1, string2, index):
    i = string1[:index]
    j = string1[index + 1:]
    new_str = i + string2 + j
    print("OUTPUT", new_str)

def FindWordCount(lst, string):
    count = 0
    for x in lst:
        if x == string:
            count = count + 1
    print("OUTPUT", count)

def ScoreFinder(list1, list2, string):
    listq = []
    listw = []
    if string in list1:
        i = list1.index(string)
        print("OUTPUT", list1[i], "got a score of", list2[i])
        
    for x in list1:
        q = x.lower()
        listq.append(q)
        
    if string in listq:
        i = list1.index(string)
        print("OUTPUT", list1[i], "got a score of", list2[i])
        
    for y in list1:
        w = x.upper()
        listw.append(w)
        
    if string in listw:
        i = list1.index(string)
        print("OUTPUT", list1[i], "got a score of", list2[i])

    else:
        print("OUTPUT player not found") 

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

#Divide a given list into differnt lists of given size
def group(l,size):    # sourcery skip: hoist-statement-from-if
    length = len(l)
    newlist = []
    newgroup = []
    j = 0
    for i in range(length):
        if(j<size - 1):
            newgroup.append(l[i])
            j += 1
        else:
            j = 0
            newgroup.append(l[i])
            newlist.append(newgroup)
            newgroup = []
    if(newgroup != []):
        newlist.append(newgroup)
    return newlist

print(group([3,4,2,4,5,2,1,3,5,2,1,4,5,2,3,4,2,1], 3))

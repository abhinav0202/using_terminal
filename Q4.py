#sort list according to string length
def lensort(x):  # sourcery skip: list-comprehension
    list1 = []
    for i in x:
        list1.append([len(i),i])
    return sorted(list1)

lista = ['aaaaaa', 'bb', 'ccc', 'dddd','e','fffffffff']
a=lensort(lista)
print([l[1] for l in a])
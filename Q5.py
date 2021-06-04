#sort files according to their extensions. 
import os

def extsort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])

file = ['first.py','2w.html','3m.js','dfg.cpp','asd.c']
newfile = extsort(file)
print(newfile)
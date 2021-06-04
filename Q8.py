#Print the reversed lines of a file

def Reverse_Content():
      Names = open("Names.txt","r")
      k=Names.readlines()
      t=reversed(k)
      for i in t:
           print(i.rstrip())

Reverse_Content()
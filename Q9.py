def reverse_slicing(s):
    return s[::-1]

textfile = open("Names.txt")
lines = textfile.readlines()
for line in lines:
    print(reverse_slicing(line))
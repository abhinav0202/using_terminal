#read, write, readline, writeline, open and close functions implemented
# sourcery skip: ensure-file-closed
Names = open("Names.txt", "w")
Names.write("Shashank\n")
Names.write("Temp\n")
Names.close()

Names = open("Names.txt", "r")
print(Names.read())
Names.close()

Names = open("Names.txt", "a")
Names.writelines(["Hello! ", "How are you?"])
Names.close()

Names = open("Names.txt", "r")
print(Names.read())
Names.close()

Names = open("Names.txt","r")
print(Names.readline())
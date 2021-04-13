file=open("demo.txt",'w')
file.write("This is the text wriiten to the file")
file.close()
file=open("demo.txt",'r')
content=file.read()
print(content)


# file=open("demo.txt",'w')
# file.write("This is the text wriiten to the file asim new")
# file.close()

file=open("demo.txt",'a')#append mode
file.write("This is the text wriiten to the file asim new")
file.close()

file=open("demo.txt",'r')
content=file.read()
print(content)


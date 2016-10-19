import re
name = input("Name of the text file: ")
fhand = open(name)
inp = fhand.read()
y = re.findall('[0-9]+',inp)
total = 0
for num in y:
    x = float(num)
    total = total + x
print (total)

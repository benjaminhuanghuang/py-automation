f = open('inputFile.txt', 'r')
print(f.read())
f.close()


# Line by line
f = open('inputFile.txt', 'r')
for line in f:
  print(line)
f.close()

# Read file as list
f = open('inputFile.txt', "r")
f_content = f.readlines()
print(f_content)
f.close()


# With
with open('inputFile.txt', 'r') as f:
   for line in f:
      print(line)



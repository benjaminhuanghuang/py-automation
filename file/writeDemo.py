newFile = open('newFile.txt', 'w')
filecontent = ["Hello, world", "a second line", "and a third line"]
for line in filecontent:
    newFile.write(line)
newFile.close()


existFile = open('newFile.txt', 'a')
filecontent = ["Hello, world", "a second line", "and a third line"]
for line in filecontent:
    newFile.write(line)
newFile.close()
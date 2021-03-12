f = open('C:\\Users\\nguye\OneDrive\\Documents\\advent-of-code\\3\\input.txt', 'r')
content = f.read()

test = content.split()
rows = len(test)
columns = len(test[0])

content = content.replace('\n','')

if test[0][0] == "#":
    counter = 1
else:
    counter = 0

for i in range(1, rows):
    index = i * 3 % columns
    if test[i][index] == "#":
        counter += 1

print(counter)
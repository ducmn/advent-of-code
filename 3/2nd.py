f = open('C:\\Users\\nguye\OneDrive\\Documents\\advent-of-code\\3\\input.txt', 'r')
content = f.read()

test = content.split()
rows = len(test)
columns = len(test[0])

content = content.replace('\n','')

if test[0][0] == "#":
    counter1 = 1
    counter2 = 1
    counter3 = 1
    counter4 = 1
    counter5 = 1
else:
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0

for i in range(1, rows):
    index1 = i % columns
    if test[i][index1] == "#":
        counter1 += 1
        
    index2 = i * 3 % columns
    if test[i][index2] == "#":
        counter2 += 1
    
    index3 = i * 5 % columns
    if test[i][index3] == "#":
        counter3 += 1
        
    index4 = i * 7 % columns
    if test[i][index4] == "#":
        counter4 += 1
    
    if i*2 <= rows:
        if test[i*2][index1] == "#":
            counter5 += 1

print(counter1 * counter2 * counter3 * counter4 * counter5)
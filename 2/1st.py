f = open('C:\\Users\\nguye\OneDrive\\Documents\\advent-of-code\\2\\input.txt', 'r')
content = f.read()
x = content.split("\n")
x.pop(-1)

# COunter
counter = 0

for i in x:
    # 3 components
    i = i.split()
    #1st
    mini, maxi = i[0].split("-")
    #2nd
    letter = i[1][0]
    #3rd
    checker = i[2].count(letter)
    if checker >= int(mini) and checker <= int(maxi):
        counter+=1

print(counter)

# Close the file
f.close()
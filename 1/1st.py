f = open('input.txt', 'r')
content = f.read()
x = content.split()

# How many numbers in the file:
length = len(x)


for i in range(length):
    first = int(x[i])
    for j in range(i, length):
        second = int(x[j])
        if first + second == 2020:
            print(first * second)
f.close()
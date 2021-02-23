f = open('input.txt', 'r')
content = f.read()
x = content.split()


length = len(x)


for i in range(length):
    first = int(x[i])
    for j in range(i, length):
        second = int(x[j])
        for k in range(j, length):
            third = int(x[k])
            if first + second + third == 2020:
                print(first * second * third)
f.close()
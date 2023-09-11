height = int(input('Input'))
number = 1
for i in range(1, height + 1):
    for j in range(1, height + 1):
        for x in range(1, number + 2):
            if i == j or i + j == height + 1:
                print(number, end='')
            else:
                print(' ', end='')
    print()
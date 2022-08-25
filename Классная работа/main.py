n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i


for i in range(n - 1):
    sum -= int(input())
print(sum)



n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()

a = int(input('a='))
b = int(input('b='))
h = int(input('h='))
x = a-b
c = int(h / x)
if a>b:
    print('через',c,'дней')
else:
    print('улитка никогда не доползёт до конца столба')
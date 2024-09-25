print('Введите число от 3 до 20: ')
x = input()
x=int(x)
p=[]
for i in range(x) :
    for j in range(x):
        if i > 0 and j > 0 and i < j:
            a = i + j
            if x % a == 0 :
                p.append(i)
                p.append(j)

print(p)


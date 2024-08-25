first = 123
second = 123
third = 123
num = int(input('Ввод в консоль 1:'))
if first == second == third:
    print(3)
elif first == second or first == third:
    print(2)
else:
    print(0)

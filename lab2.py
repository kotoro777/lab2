f = open("numbers.txt", "r")

text = f.read()
numbers = []
numbers = text.split()
print('Исходные числа: ', numbers)

print('Обработанные числа: ', end = '')
for i in numbers:
    if int(i) % 2 == 0:
        _num = ''
        for i2 in i:
            if i2 in _num:
                continue
            else:
                _num+=i2
        print(_num,  end = ', ')

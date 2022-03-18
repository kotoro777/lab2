import time
start = time.time()                 # запускаем таймер
with open('numbers.txt', 'r') as f: # открываем файл
    data = f.read().split()         # считываем каждый строчный символ в файле
    s = ''
    for i in data:
        if int(i) % 2 == 0:         # находим четное число
            if len(set(list(i))) == len(i): # проверяем нет ли в i повторяющихся цифр
                s += i              #
            else:
                s += ''.join(sorted(set(list(i)), key=i.index)) # убираем повторяющие цифры из числа
            s += ' '                #
    finish = time.time()
    result = finish - start         # отключаем таймер
    print(s, "Program time: " + str(result) + " seconds.") # выводим результат программы

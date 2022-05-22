import time

buffer_len = 1  # Размер буфера чтения
s = []  # Массив в котором будут храниться числа

try:
    start = time.time()  # Запускаем таймер
    with open("text.txt", "r") as file:  # Открываем файл
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)  # Читаем первый блок

        if not buffer:  # Если файл пустой
            print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")

        while buffer:  # Пока файл не пустой

            while (buffer < '0' or buffer > '9') and buffer != '.' and buffer:  # Ищем начало числа
                buffer = file.read(buffer_len)  # Читаем очередной блок

            while (buffer >= '0' and buffer <= '9') or buffer == '.' and buffer:  # Обрабатываем число
                s.append(buffer)
                buffer = file.read(buffer_len)  # Читаем очередной блок
                s == []

            if s != []:
                temp = ''.join(s)
                try:
                    if int(temp) % 2 == 0:  # Проверяем число четное
                        temp2 = ''
                        for j in temp:
                            if temp2.find(j) == -1:
                                temp2 = temp2 + j
                        print(temp2)
                    else:
                        print(temp)
                except:
                    print(temp)
            s = []
    finish = time.time()
    result = finish - start  # Отключаем таймер
    print("Program time: " + str(result) + " seconds.")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

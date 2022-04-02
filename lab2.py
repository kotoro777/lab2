import itertools

more_max_buffer_len = False                 # максимальный размер рабочего буфера
max_buffer_len = 100                        # максимальный размер рабочего буфера
buffer_len = 1                              # размер буфера чтения
work_buffer = ""                            # рабочий буфер

try:
    with open("text.txt", "r") as file:                    # открываем файл
        print("\n-----Результат работы программы-----\n")  # читаем первый блок
        buffer = file.read(buffer_len)

        if not buffer:                                     # если файл пустой
            print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")

        while buffer:                                      # пока файл не пустой
            buffer = file.readlines(buffer_len)            # читаем очередной блок
            buffer = list(itertools.chain(*[num.split() for num in buffer]))
            if not buffer:
                break

            for num in buffer:                              # обрабатываем числа
                if int(num) % 2 == 0:                       # находим четное число
                    unique_num = list(set(list(num)))

                    work_buffer = ""
                    for i in num:
                        if i in unique_num:
                            work_buffer += i
                            unique_num.remove(i)

                    print(work_buffer)
                else:
                    print(num)

            if len(work_buffer) >= max_buffer_len:           # Если буфер переполнен и в нем нет цифр
                print("\nФайл text.txt содержит блок цифр, превышающий максимальный размер буфера = " + str(max_buffer_len) + " символов.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                more_max_buffer_len = True

            if more_max_buffer_len:
                break

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

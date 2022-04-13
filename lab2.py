
buffer_len = 1          # размер буфера чтения

try:
    with open('text.txt', 'r') as file:   # открываем файл
        print("\n-----Результат работы программы-----\n")

        while True:      # бесконечный цикл для чтения символов из файла

            char = None  # переменная символа
            number = ""  # переменная числа

            while True:     # цикл для получения числа из посимволного чтения
                char = file.read(buffer_len)    # читаем блок

                if char == '':  # проверяем конец файла
                    break
                elif char == " ":
                    break
                elif char == "\n":
                    break
                number += char          # складываем в переменную символ

            if number.isdigit():

                if int(number) % 2 == 0:    # проверяем число четное

                    unique_num = list(set(list(number)))   # получаем список уникальных цифр числа
                    new_num = ""                           # переменная новая число после удаления повторных цифр

                    for n in number:    # проходимся по всем цифрам числа

                        if n in unique_num:        # если цифра есть в списке уникальных цифр числа

                            new_num += n           # добавляем цифру в новое число
                            unique_num.remove(n)   # удалем из списка уникальных цифр числа

                    print(new_num)
                else:
                    print(number)

            if char == '':  # проверка конец ли это файла
                break

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

import cProfile
import time

buffer_len = 1          # размер буфера чтения

def task():
    try:
        start = time.time()                   # запускаем таймер
        with open('text.txt', 'r') as file:   # открываем файл
            print("\n-----Результат работы программы-----\n")

            while True:      # бесконечный цикл для чтения символов из файла

                char = None  # переменная символа
                number = ""  # переменная числа

                while True:     # цикл для получения числа из посимволного чтения
                    char = file.read(buffer_len)    # читаем очередной блок

                    if char == '':  # конец файла
                        break
                    elif char == " ":
                        break
                    elif char == "\n":
                        break
                    number += char          # складываем в переменную символ

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
                finish = time.time()
                result = finish - start  # отключаем таймер
            print("Program time: " + str(result) + " seconds.")

    except FileNotFoundError:
        print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

def main():
    task()

if __name__ == '__main__':
    cProfile.run('main()')

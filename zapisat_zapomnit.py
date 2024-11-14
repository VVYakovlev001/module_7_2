


info = [
    'Text for tell.',
    'Используйте кодировку utf - 8',
    'Because there are 2 languages!',
    'Спасибо!',
    ]
def custom_write(file_name,strings):# функция custom_write(file_name, strings)
    string_dist = {} # список строк для записи.
    string_num = 0 #
    file = open(file_name,'a+',encoding='utf-8') # Открываем и записываем file
    for string in strings:
        byte_position = file.tell()# возвращает текущую позицию указателя
        # чтения/записи в файле в байтах.
        string_num += 1
        file.write(string + '\n')# записывает в файл строку str.
        # Метод возвращает целое число - количество записанных байт.
        string_dist[(string_num,byte_position)] = string
        file.close() # Закрываем файл
        return string_dist # возвращаем string_dist



result = custom_write('test.txt', info)
for elem in result.items():
        print(elem)

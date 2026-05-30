import os
import shutil
import time

logo = '''
 ____________________________________________________

|                                                    |
|   ██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗  |
|  ██╔════╝ ██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗ |
|  ╚█████╗  ██║   ██║██████╔╝   ██║   █████╗  ██████╔╝ |
|   ╚═══██╗ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗ |
|  ██████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║ |
|  ╚═════╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ |
|                                                    |
|-- [    WINDOWS FILE MANAGER      ] -- [ v1.0.0 ] --|
|____________________________________________________|
'''

print(logo)

PATH = input('\n>> Введите путь к папке (0 для выхода): ')

if PATH == '0':
    print('[Sorter] Завершение работы...')
    time.sleep(1)
    exit(0)

# возможные расщирения
EXTENSIONS = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', 'doc'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Installers': ['.exe', '.msi'],
    'Text': ['.txt', '.rtf', '.md'],
    'Sound': ['.mp3'],
    'Video': ['.mp4']
}


# колво папок, файлов, список с файлами
dirs = 0
files = 0
file_list = []

try:
    # перебор всех элементов по пути, разделение на папки и файлы
    for i in os.listdir(PATH):
        file_path = os.path.join(PATH, i)
        if os.path.isdir(file_path):
            dirs += 1
        else:
            files += 1
            file_list.append(i)

            # разделяем название i-того файла и расширение
            name, ext = os.path.splitext(i)
            ext = ext.lower()

            # флаг для проверки на успех сортировки
            sorted_succes = False

            # просмотр категории и расширения файла для его распределения
            for category, extensions in EXTENSIONS.items():
                if ext in extensions:
                    # если расщирение есть - создает папку
                    category_dir = os.path.join(PATH, category)
                    os.makedirs(category_dir, exist_ok = True)

                    # перемещение файла в папку
                    shutil.move(file_path, os.path.join(category_dir, i))
                    print(f'[Sorter] Файл {i} перемещен в {category}')

                    # успешная сортировка
                    sorted_succes = True
                    break

            # отправляет неопределенные файлы папку Other
            if not sorted_succes:
                other_dir = os.path.join(PATH, 'Other')
                os.makedirs(other_dir, exist_ok = True)
                shutil.move(file_path, os.path.join(other_dir, i))
                
except Exception as e:
    print(f'[Sorter] При вводе пути возникла ошибка: {e}')

print(f'[Sorter] Папок: {dirs}, Файлов: {files}')
input('\n[Sorter] Работа завершена. Нажмите ENTER для выхода...')

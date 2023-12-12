import os



import fnmatch
import sys


def dir(path):
    files = os.listdir(path) #получаем список файлов и папок в указанном пути
    directories = []
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            directories.append(file)

    if len(directories) == 0:
        print('В данном пути директорий нет.')
    else:
        cnt = 0
        print(f'Директории по указанному пути - {path}:')
        for directory in directories:
            cnt += 1
            print(f'{cnt}. {directory}')


def findFiles(target, path):
    target_files = []

    # перебираем все элементы в текущем каталоге
    for item in os.listdir(path):
        # формируем полный путь до элемента
        item_path = os.path.join(path, item)

        # если это каталог, идем в него
        if os.path.isdir(item_path):
            target_files += find_files(target, item_path)

        # если это файл и его имя содержит target, добавляем в список
        elif os.path.isfile(item_path) and fnmatch.fnmatch(item, '*{}*'.format(target)):
            target_files.append(item_path)

    return target_files



def acceptcommand():
    """

    :return: number of choice
    """
    NUM = ['1', '2', '3', '4', '5', '6', '7']
    choice = 0
    control = True
    while control:
        print('1.Просмотр каталога\n'
              '2.На уровень вверх\n'
              '3.На уровень вниз\n'
              '4.Количество файлов и каталогов\n'
              '5.Размер текущего каталога (в байтах)\n'
              '6.Поиск файла\n'
              '7.Выход из программы\n')
        choice = input('Выберите пункт меню: ')
        if choice not in NUM:
            print('\nНекорректно указан номер пункта. Повторите еще раз.')
            control = True
        else:
            control = False

    return int(choice)




def moveUp():
    curnt_dir = os.getcwd()
    parnt_dir = os.path.dirname(curnt_dir)
    os.chdir(parnt_dir)
    

def countBytes(dir):
    total_size = 0
    for path, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def runCommand(command, currentDir):
    if command == 1:
        path = input('Введите директорию каталога: ')
        dir(path)
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:
        count = countFiles(currentDir)
        print("Количество файлов:", count)
    elif command == 5:
        bytes_count = countBytes(currentDir)
        print("Суммарный объем файлов (в байтах):", bytes_count)
    if command == 6:
        target = input("Введите имя файла для поиска: ")
        findFiles(target, currentDir)
    if command == 7:
        sys.exit('Работа программы завершена.')


def moveDown(currentDir):
    sub_dir = input("Введите имя подкаталога: ")
    new_dir = os.path.join(currentDir, sub_dir)
    if os.path.exists(new_dir) and os.path.isdir(new_dir):
        os.chdir(sub_dir)
    else:
        print("Ошибка: указанный каталог не существует.")


def countFiles(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count




if __name__ == '__main__':
    current_dir = os.getcwd()
    print(current_dir)
    runCommand(acceptcommand(), current_dir)

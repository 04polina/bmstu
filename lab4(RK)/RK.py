import os

def sort_by_num(record):
    return record['num']
def sort_by_task(record):
    return record['task']
def sort_by_date(record):
    return record['date']
def sort_by_time(record):
    return record['time']
def sort_by_priority(record):
    return record['priority']
def sort_by_status(record):
    return record['status']

def print_notebook(name):
    print("Отсортировать по\n"
          "1: Номеру\n"
          "2: Заданию\n"
          "3: Времени\n"
          "4: Дате\n"
          "5: Приоритету\n"
          "6: Статусу\n")
    k = int(input())
    records = list()
    with open(name + ".csv", "r", encoding="utf8") as file:
        string = file.readline()
        while string:
            record = dict()
            record['num'], record['task'], record['time'], record['date'], record['priority'], record['status'] = string.split(',')
            records.append(record)
            string = file.readline()

    match k:
        case 1:
            records.sort(key=sort_by_num)
        case 2:
            records.sort(key=sort_by_task)
        case 3:
            records.sort(key=sort_by_time)
        case 4:
            records.sort(key=sort_by_date)
        case 5:
            records.sort(key=sort_by_priority)
        case 6:
            records.sort(key=sort_by_status)

    for i in records:
        print(','.join(i.values()), end='')


def watch_notepads_list():
    for obj in os.listdir():
        splited = obj.split('.')
        form = splited[len(splited) - 1]
        if form == 'csv':
            print(obj)


def print_str_to_file(file, string):
    file.seek(0, 2)
    file.write(string)
    file.write('\n')
    file.flush()


def create_notepad(name):
    with open(name + ".csv", "a+", encoding="utf8") as file:
        while True:
            print("0: Выйти\n"
                  "1: Вывести содержимое\n"
                  "2 ___: Добавить запись")
            input_string = input().split()
            command = int(input_string[0])
            match command:
                case 0:
                    break
                case 1:
                    print_notebook(name)
                case 2:
                    print_str_to_file(file, " ".join(input_string[1:]))


def delete_record(name, record):
    with open(name+".csv", "r", encoding="utf8") as f:
        lines = f.readlines()
    new_lines = list()
    for i in range(len(lines)):
        if lines[i][0] != record:
            new_lines.append(lines[i])
    with open(name+".csv", "w", encoding="utf8") as f:
        f.writelines(new_lines)
        f.flush()



def change_notepad(name):
    print_notebook(name)
    with open(name + ".csv", "a+", encoding="utf8") as file:
        while True:
            print("0: Выйти\n"
                  "1: Вывести содержимое\n"
                  "2 ___: Добавить запись\n"
                  "3 (номер записи): Удалить запись"
                  )
            input_string = input().split()
            command = int(input_string[0])
            match command:
                case 0:
                    break
                case 1:
                    print_notebook(name)
                case 2:
                    print_str_to_file(file, " ".join(input_string[1:]))
                case 3:
                    delete_record(name, input_string[1])


def delete_notepad(name):
    os.remove(name+".csv")
    pass


while True:
    print("Введите команду \n"
          "1: Посмотреть список существующих блокнотов\n"
          "2 [name]: Создать новый блокнот\n"
          "3 [name]: Изменить существующий блокнот\n"
          "4 [name]: Удалить существующий блокнот\n"
          "0: Выйти")
    input_string = input().split()
    command = int(input_string[0])
    match command:
        case 0:
            break
        case 1:
            watch_notepads_list()
        case 2:
            create_notepad(input_string[1])
        case 3:
            change_notepad(input_string[1])
        case 4:
            delete_notepad(input_string[1])

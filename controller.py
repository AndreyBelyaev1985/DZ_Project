from find_data import find
from process_data import build_compl
from process_data import build_planned


def project():
    work = True
    while work:
        task = request()
        if task == 3:
            work = False
        elif task == 1:
            var_choice = plann_or_compl()
            if var_choice == "p":
                user_input = str(input("Введите запланированную задачу в формате (Дата задача примечание): "))
                print(build_planned(user_input))
                print("Запись добавдена!")
                project()
            elif var_choice == "c":
                user_input = str(input("Введите выполненую задачу в формате (Дата задача примечание): "))
                build_compl(user_input)
                print("Запись добавдена!")
                project()

        elif task == 2:
            crit_find = str(input("Введите критерий поиска: "))
            print(find(crit_find))
            project()
    else:
        print("Всего доброго!")
def request():
    print("Планируем дела")
    user_request = int(input("Записать задачу - 1 Найти задачу - 2 Выход - 3 :"))

    return user_request

def plann_or_compl():
    user_choice = str(input("Запись в запланированные - p Запись в выполниные - c"))
    return user_choice


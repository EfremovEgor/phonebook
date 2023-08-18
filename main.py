import sys
from utils import *


def add_contact_handler() -> None:
    """
    Handles add contact event
    """
    print(
        """
            ДОБАВЛЕНИЕ КОНТАКТА
        """,
    )
    to_add = dict()
    while True:
        print(
            f"""
    Выберите поле:
        [1] Фамилия: {to_add.get("surname","")}
        [2] Имя: {to_add.get("name","")}
        [3] Отчество: {to_add.get("middlename","")}
        [4] Организация: {to_add.get("company","")}
        [5] Мобильный телефон: {to_add.get("mobile_phone_number","")}
        [6] Рабочий телефон: {to_add.get("work_phone_number","")}
        [7] Добавить
        [8] В меню
            """
        )
        answer = int(input("\nВведите номер поля:\n"))
        if answer not in range(1, 9):
            continue
        if answer == 7:
            if not all([item in list(to_add.keys()) for item in FIELDNAMES]):
                print("Отсутствуют данные")
                continue
            add_contact(to_add)
            to_add.clear()
            continue
        if answer == 8:
            break
        if answer == 5 or answer == 6:
            while True:
                data = input("\nВведите значение:\n")
                if validate_phone_number(data):
                    to_add[FIELDNAMES[answer - 1]] = data
                    break
                print("\nНеверный формат телефона")
        else:
            to_add[FIELDNAMES[answer - 1]] = input("\nВведите значение:\n")


def investigate_contacts_handler() -> None:
    """
    Handles investigate contact event
    """
    print(
        """
            КОНТАКТЫ
        """,
    )
    counter = 0
    contacts = chunkify_list(get_contacts(), CONTACTS_PER_PAGE)
    max_counter = len(contacts)
    while True:
        print_contacts(contacts[counter])

        print(
            f"""
                    {counter+1} СТРАНИЦА
        """,
            end="",
        )
        print(
            """
    Выберите действие:
        [1] Следующая страница
        [2] Предыдущая страница
        [3] В меню """
        )
        answer = int(input("Введите номер действия:\n"))
        if answer == 3:
            break
        elif answer == 1:
            if counter + 1 < max_counter:
                counter += 1
        elif answer == 2:
            if counter > 0:
                counter -= 1


def search_contacts_handler() -> None:
    """
    Handles search contact event
    """
    print(
        """
            ПОИСК КОНТАКТОВ
        """,
    )
    to_search = dict()
    while True:
        print(
            f"""
    Выберите поле:
        [1] Фамилия: {to_search.get("surname","")}
        [2] Имя: {to_search.get("name","")}
        [3] Отчество: {to_search.get("middlename","")}
        [4] Организация: {to_search.get("company","")}
        [5] Мобильный телефон: {to_search.get("mobile_phone_number","")}
        [6] Рабочий телефон: {to_search.get("work_phone_number","")}
        [7] Поиск
        [8] В меню
            """
        )
        answer = int(input("\nВведите номер поля:\n"))
        if answer not in range(1, 9):
            continue
        if answer == 7:
            contacts = search_contact(to_search)

            print_contacts(contacts) if contacts else print("Ничего не найдено")
            if not contacts:
                continue
            while True:
                print(
                    f"""
        Выберите поле:
            [1] Изменить
            [2] Удалить
            [3] Назад
                """
                )
                answer = int(input("\nВведите номер действия:\n"))
                if answer == 2:
                    answer = int(
                        input("\nВведите порядковый номер контакта для удаления:\n")
                    )
                    try:
                        delete_contact(contacts[answer - 1])
                    except IndexError:
                        print("Неверный номер")
                        continue
                if answer == 1:
                    answer = int(
                        input("\nВведите порядковый номер контакта для изменения:\n")
                    )
                    try:
                        edit_contact_handler(contacts[answer - 1])
                    except IndexError:
                        print("Неверный номер")
                        continue
                if answer == 3:
                    break
            to_search.clear()
            continue
        if answer == 8:
            break
        to_search[FIELDNAMES[answer - 1]] = input("\nВведите значение:\n")


def edit_contact_handler(previous_contact: dict) -> None:
    """
    Handles edit contact event

    Args:
        previous (dict): Contact
    """
    print(
        """
            Изменение контакта
        """,
    )
    to_edit = previous_contact.copy()
    while True:
        print(
            f"""
    Выберите поле:
        [1] Фамилия: {to_edit.get("surname","")}
        [2] Имя: {to_edit.get("name","")}
        [3] Отчество: {to_edit.get("middlename","")}
        [4] Организация: {to_edit.get("company","")}
        [5] Мобильный телефон: {to_edit.get("mobile_phone_number","")}
        [6] Рабочий телефон: {to_edit.get("work_phone_number","")}
        [7] Подтвердить
        [8] Назад
            """
        )
        answer = int(input("\nВведите номер поля:\n"))
        if answer not in range(1, 9):
            continue
        if answer == 7:
            if not all([item in list(to_edit.keys()) for item in FIELDNAMES]):
                print("Отсутствуют данные")
                continue
            edit_contact(previous_contact, to_edit)

            continue
        if answer == 8:
            break
        if answer == 5 or answer == 6:
            while True:
                data = input("\nВведите значение:\n")
                if validate_phone_number(data):
                    to_edit[FIELDNAMES[answer - 1]] = data
                    break
                print("\nНеверный формат телефона")
        else:
            to_edit[FIELDNAMES[answer - 1]] = input("\nВведите значение:\n")


def main() -> None:
    """
    Handles main menu events
    """
    answer_to_function = {
        1: investigate_contacts_handler,
        2: add_contact_handler,
        3: search_contacts_handler,
        4: sys.exit,
    }
    print(
        """
            ДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННЫЙ СПРАВОЧНИК
        """,
        end="",
    )
    while True:
        print(
            """
    Выберите действие:
        [1] Просмотреть контакты
        [2] Добавить новый контакт
        [3] Поиск/Изменение/Удаление контактов
        [4] Выход
            """
        )
        answer = int(input("Введите номер действия:\n"))
        if answer not in list(answer_to_function.keys()):
            print("\nНеверный номер\n")
            continue
        answer_to_function[answer]()


if __name__ == "__main__":
    main()

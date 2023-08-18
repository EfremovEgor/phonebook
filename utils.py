import csv
import os

import copy
from settings import *


def represent_contact(contact: dict) -> str:
    """
    Represents given contact as string

    Args:
        contact (dict): Contact

    Returns:
        String representation of given contact
    """
    return f"""
                    {contact['name']} {contact['surname']} {contact['middlename']}
                
    Организация:{contact['company']}
    Личный телефон:{contact['mobile_phone_number']}
    Рабочий телефон:{contact['work_phone_number']}"""


def print_contacts(contacts: list[dict]) -> None:
    """
    Prints given contacts in stdout

    Args:
        contacts (list[dict]): Contacts list
    """
    for contact in contacts:
        print(represent_contact(contact))


def search_contact(contact: dict) -> list[dict] | list:
    """
    Searches suitable contacts by given fields in contacts file and returns them

    Args:
        contact (dict): Contact

    Returns:
        List of found contacts
    """
    data = list()
    for item in get_contacts():
        for key, value in contact.items():
            if item[key] != value:
                break
        else:
            data.append(item)
    return data


def write_contacts(contacts: list[dict]) -> None:
    """
    Writes given contacts to contacts file

    Args:
        contacts (dict): Contacts
    """
    if not os.path.exists(CONTACTS_FILE_PATH):
        initialize_contacts_file()
    with open(CONTACTS_FILE_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="raise")
        writer.writeheader()
        writer.writerows(contacts)


def edit_contact(previous_contact: dict, new_contact: dict) -> None:
    """
    Replaces given previous contact by new contact in the contacts file

    Args:
        previous_contact (dict): Contact
        new_contact (dict): Contact
    """
    contacts = get_contacts()
    new_contacts = [
        item if item != previous_contact else new_contact for item in contacts
    ]
    write_contacts(new_contacts)


def delete_contact(contact: dict) -> None:
    """
    Deletes given contact from contacts file

    Args:
        contact (dict): Contact
    """
    contacts = get_contacts()
    new_contacts = [item for item in contacts if item != contact]
    write_contacts(new_contacts)


def chunkify_list(lst: list, amount: int) -> list[list]:
    """
    Splits list into multiple list of given length

    Args:
        lst (list): List
        amount (int): maximum amount of items contained in final chunks

    Returns:
        List of lists
    """
    lst = copy.deepcopy(lst)
    final_list = list()
    counter = 0
    for item in lst:
        if not counter % amount:
            final_list.append(list())
        final_list[counter // amount].append(item)
        counter += 1
    return final_list


def add_contact(contact: dict) -> None:
    """
    Adds given contact to contacts file

    Args:
        contact (dict): Contact
    """
    if not os.path.exists(CONTACTS_FILE_PATH):
        initialize_contacts_file()
    with open(CONTACTS_FILE_PATH, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="raise")
        writer.writerow(contact)


def validate_phone_number(number: str) -> bool:
    """
    Validates phone number by regex

    Args:
        number (int): Phone number

    Returns:
        True or False
    """
    return bool(PHONE_REGEX.match(number))


def get_contacts() -> list[dict]:
    """
    Reads contacts from contacts file

    Returns:
        Contacts
    """
    with open(CONTACTS_FILE_PATH, "r") as f:
        data = list()
        reader = csv.DictReader(f)
        for item in reader:
            data.append(item)
    return data


def initialize_contacts_file() -> None:
    """
    Makes empty contacts file
    """
    with open(CONTACTS_FILE_PATH, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=FIELDNAMES,
        )
        writer.writeheader()

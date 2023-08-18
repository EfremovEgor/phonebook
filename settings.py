import re
import os

FIELDNAMES = (
    "surname",
    "name",
    "middlename",
    "company",
    "mobile_phone_number",
    "work_phone_number",
)
CURRENT_DIRECTORY = os.getcwd()
CONTACTS_FILE_PATH = os.path.join(CURRENT_DIRECTORY, "contacts.csv")
PHONE_PATTERN = "\A((\+\d)|(\d))\(?\d{3}\)?\d{3}\-?\d{2}\-?\d{2}\Z"
PHONE_REGEX = re.compile(PHONE_PATTERN)
CONTACTS_PER_PAGE = 2

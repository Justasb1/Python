import random
import datetime


def get_person_code_checksum(code: str) -> int:
    numbers = list(map(int, code))
    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    checksum = sum(x * i for x, i in zip(numbers, factors)) % 11
    if checksum == 10:
        factors = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        checksum = sum(x * i for x, i in zip(numbers, factors)) % 10
    return checksum


def generate_person_code(
    *,
    dob: datetime.datetime = None,
    gender: int = None,  # 0 - male, 1 - female
    num: int = None,  # between 1 and 999, including both ends
) -> str:
    if dob is None:
        now = datetime.datetime.now()
        dob = random.randint(
            int((now - datetime.timedelta(days=365) * 105).timestamp()),
            int(now.timestamp()),
        )
        dob = datetime.date.fromtimestamp(dob)

    if dob.year < 1801:
        raise ValueError("dob year must be at least 1801")

    if gender is None:
        gender = random.randint(0, 1)
    century = dob.year // 100 - 18
    cender = century * 2 + gender + 1

    if num is None:
        num = random.randint(1, 999)

    code = f'{cender}{dob:%y%m%d}{num:03}'
    checksum = get_person_code_checksum(code)

    return f'{code}{checksum}'

generate_person_code()
from typing import List


def find_addition(list_of_numbers: List[int], k: int) -> bool:
    for idx, number in enumerate(list_of_numbers):
        for iterate_number in list_of_numbers[idx:]:
            if number + iterate_number == k:
                return True
    return False

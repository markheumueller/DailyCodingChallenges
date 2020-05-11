from typing import List
from math import prod


def get_iterated_products(input_sequence: List[int]) -> List[int]:
    product_array: List[int] = []
    for idx, i in enumerate(input_sequence):
        product_array.append(prod(input_sequence[:idx]+input_sequence[idx+1:]))
    return product_array

import numpy as np
from matplotlib import pyplot as plt


import matplotlib

def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        return num * factorial(num - 1)


def read_csv(filepath: str):
    row = [1]
    column = [1]
    return row, column

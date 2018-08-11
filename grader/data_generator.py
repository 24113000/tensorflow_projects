from random import uniform
import numpy as np
from rules import *


def determine_group(x):
    if rule_1(x):
        return 1

    if rule_2(x):
        return 2

    if rule_3(x):
        return 3

    return 0


def generator_one_item():
    x = np.zeros(40)
    for i in range(40):
        x[i] = uniform(-1, 1)
    y = determine_group(x)
    return x, y


def generator(number_items):
    x_list = np.array([], dtype=float)
    y_list = np.zeros(number_items, dtype=int)
    for i in range(number_items):
        x, y = generator_one_item()
        np.append(x_list, x)
        y_list[i] = y

    return x_list, y_list


def main():
    x, y = generator(10)
    #print(x)
    print(y)


if __name__ == "__main__":
    main()


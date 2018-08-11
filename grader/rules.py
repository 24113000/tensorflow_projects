def rule_1(x):
    for i in range(3):
        if x[i] % 2 != x[i]:
            return False
    return True


def rule_2(x):
    counter = 0
    for i in range(40):
        if (x[i] >= -0.15) and (x[i] <= 0.15):
            counter += 1
    return counter >= 8


def rule_3(x):
    counter = 0
    for i in range(40):
        if (x[i] * 100) >= 50:
            counter += 1
    return counter >= 14

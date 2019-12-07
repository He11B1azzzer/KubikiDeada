def generating(coef, power):
    if power == 0:
        return [1]
    elif power % 2 == 0:
        tmp = generating(coef, power / 2)
        ans = [0] * (2 * len(tmp) - 1)
        for i1, v1 in enumerate(tmp):
            for i2, v2 in enumerate(tmp):
                ans[i1 + i2] += v1 * v2
        return ans
    else:
        tmp = generating(coef, power - 1)
        ans = [0] * (len(tmp) + len(coef) - 1)
        for i1, v1 in enumerate(tmp):
            for i2, v2 in enumerate(coef):
                ans[i1 + i2] += v1 * v2
        return ans

def probability(dice_number, sides, target):
    # https://en.wikipedia.org/wiki/Generating_function
    try:
        return round(float(generating([0] + [1] * sides, dice_number)[target]) / (sides ** dice_number), 4)
    except IndexError:
        return 0.
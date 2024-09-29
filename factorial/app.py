def fac(num: int):
    if num == 0:
        return 1
    return fac(num - 1) * num


print(fac(4))

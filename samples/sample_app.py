# def add_calc(a, b):
#     return a + b


def add_calc(a: int, b: int) -> int:
    if int != type(a):
        return False
    if int != type(b):
        return False
    return a + b

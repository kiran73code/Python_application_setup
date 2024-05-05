"""
 simple python code to demonstrate code style usage
"""


def bit_manipulation(num: int, position: int):
    """
    :param n:
    :param i:
    """
    position -= 1
    if (num & 1 << position) > 0:
        get_bit = 1
    else:
        get_bit = 0
    set_bit = num | 1 << position
    clear_bit = num & ~(1 << position)
    print(get_bit, set_bit, clear_bit)


if __name__ == "__main__":
    n = int(input())
    i = int(input())
    bit_manipulation(n, i)

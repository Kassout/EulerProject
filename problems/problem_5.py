import math


def problem():
    """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    result = 1
    for i in range(1, 20 + 1):
        result = (result * i) / math.gcd(int(result), int(i))
    return int(result)


if __name__ == "__main__":
    value = problem()
    print(value)

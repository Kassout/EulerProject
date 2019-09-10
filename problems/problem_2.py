import math


def problem():
    """By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms."""
    fibonacci_number = 0
    index = 1
    result = 0
    phi = (1 + math.sqrt(5)) / 2
    phi_p = -1 / phi
    while fibonacci_number <= 4_000_000:
        fibonacci_number = (1 / math.sqrt(5)) * (phi**index - phi_p**index)
        if int(fibonacci_number) % 2 == 0:
            result += int(fibonacci_number)
        index += 1
    return result


if __name__ == "__main__":
    value = problem()
    print(value)

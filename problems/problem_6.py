
def problem():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square
    of the sum."""
    square_sum = sum([value**2 for value in range(1, 101)])
    square_of_the_sum = sum([value for value in range(1, 101)])**2
    result = square_of_the_sum - square_sum
    return result


if __name__ == "__main__":
    value = problem()
    print(value)

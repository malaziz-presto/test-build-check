from functools import reduce


class ArithmeticOperations:
    def sum_numbers(input: list[int]) -> int:
        return sum(input)

    def multiply_numbers(input: list[int]) -> int:
        return reduce(lambda x, y: x * y, input)

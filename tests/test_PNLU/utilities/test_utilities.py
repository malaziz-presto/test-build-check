from PNLU.utilities.arithmetic_operations import ArithmeticOperations


class TestArithmeticOperations:
    def test_sum(self) -> None:
        assert ArithmeticOperations.sum_numbers([1, 2, 3]) == 6

    def test_multiply(self) -> None:
        assert ArithmeticOperations.multiply_numbers([1, 2, 3]) == 6

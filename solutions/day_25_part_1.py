from itertools import zip_longest

SNAFU_DIGITS = ["--", "-0", "-1", "-2", "=", "-", "0", "1", "2", "1=", "1-", "10", "11"]


class SnafuNumber:
    def __init__(self, string: str) -> None:
        self.digits = list(string)

    def adder(self, digit_1, digit_2, digit_3):
        id_1 = SNAFU_DIGITS.index(digit_1)
        id_2 = SNAFU_DIGITS.index(digit_2)
        id_3 = SNAFU_DIGITS.index(digit_3)
        added_index = id_1 + id_2 + id_3 - 2 * SNAFU_DIGITS.index("0")
        result = SNAFU_DIGITS[added_index]
        if len(result) == 1:
            return "0" + result
        else:
            return result

    def __add__(self, other: "SnafuNumber"):
        result = ""
        carry = "0"
        for digit_1, digit_2 in zip_longest(reversed(self.digits), reversed(other.digits), fillvalue="0"):
            res = self.adder(digit_1, digit_2, carry)
            carry = res[0]
            digit = res[-1]
            result = digit + result
        if carry != "0":
            result = carry + result
        return SnafuNumber(result)

    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

    def __str__(self) -> str:
        return ''.join(self.digits)

    def __repr__(self) -> str:
        return ''.join(self.digits)


def solution(raw_input: str):
    snafu_numbers = [SnafuNumber(str(number)) for number in raw_input.splitlines()]

    return str(sum(snafu_numbers))

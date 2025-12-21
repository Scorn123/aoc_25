from src.utils.input_reader import read_input


class IdChecker:

    def __init__(self):
        self.counter_1 = 0
        self.counter_2 = 0

    def process_inputs(self, inputs: list[str]):
        for s in inputs:
            self._process_input(s)

    def _process_input(self, s: str):
        low, high = map(int, s.split("-"))
        self.count_valid_id(low, high)

    def count_valid_id(self, low: int, high: int):
        for n in range(low, high + 1):
            if self.is_invalid_id_1(n):
                self.counter_1 += n
            if self.is_invalid_id_2(n):
                self.counter_2 += n

    @staticmethod
    def is_invalid_id_1( n: int) -> bool:
        s = str(n)
        length = len(s)

        # must be even length
        if length % 2 != 0:
            return False

        half = length // 2
        return s[:half] == s[half:]

    @staticmethod
    def is_invalid_id_2( n: int) -> bool:
        s = str(n)
        length = len(s)

        for unit_len in range(1, length // 2 + 1):
            if length % unit_len != 0:
                continue

            unit = s[:unit_len]
            repeats = length // unit_len

            if repeats >= 2 and unit * repeats == s:
                return True

        return False

    def print_solution(self):
        print(f"Solution Puzzle 1: {self.counter_1}")
        print(f"Solution Puzzle 2: {self.counter_2}")


def main():
    id_checker = IdChecker()
    id_checker.process_inputs(read_input(2, separator=","))
    id_checker.print_solution()


if __name__ == "__main__":
    main()

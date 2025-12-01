from src.utils.input_reader import read_input
from typing import Tuple


class DialSolver:

    def __init__(self, start_position: int = 50, max_value: int = 99):
        self.position = start_position
        self.amount_values = max_value + 1
        self.counter_zero = 0

    def process_inputs(self, inputs: list[str]):
        for s in inputs:
            self._process_input(s)

    def _process_input(self, s: str):
        letter, digit = self._split_letter_number(s)

        if letter == "L":
            self.position = (self.position - digit) % self.amount_values

        if letter == "R":
            self.position = (self.position + digit) % self.amount_values

        if self.position == 0:
            self.counter_zero += 1

    @staticmethod
    def _split_letter_number(s: str) -> Tuple[str, int]:
        if s is None:
            raise ValueError("Input must be a string")
        s = s.strip()
        if len(s) < 2:
            raise ValueError("Input too short; expected at least 2 characters")

        letter, digit = s[0], s[1:]
        if letter not in ["L", "R"]:
            raise ValueError("First character must either `L` or `R`")
        if not digit.isdigit():
            raise ValueError("Remaining characters must be a digit")

        return letter, int(digit)

    def print_solution(self):
        print(f"The dial point {self.counter_zero} times to zero.")


def main():
    dial_solver = DialSolver()
    dial_solver.process_inputs(read_input(1, 1))
    dial_solver.print_solution()


if __name__ == "__main__":
    main()

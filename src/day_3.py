from src.utils.input_reader import read_input

PUZZLE_1_K = 2
PUZZLE_2_K = 12

class JoltSelector:

    def __init__(self):
        self.max_battery_1 = 0
        self.max_battery_2 = 0

    def process_inputs(self, inputs: list[str]):
        for s in inputs:
            self.max_battery_1 += self.calculate_max_bat(s,PUZZLE_1_K)
            self.max_battery_2 += self.calculate_max_bat(s,PUZZLE_2_K)

    @staticmethod
    def calculate_max_bat( s: str, bat_length: int) -> int:
        n = len(s)
        remove = n -bat_length
        stack = []

        for ch in s:
            while remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                remove -= 1
            stack.append(ch)

        if remove > 0:
            stack = stack[:-remove]

        return int(''.join(stack[:bat_length] ))

    def print_solution(self):
        print(f"Solution Puzzle 1: {self.max_battery_1}")
        print(f"Solution Puzzle 2: {self.max_battery_2}")


def main():
    jolt_selector = JoltSelector()
    jolt_selector.process_inputs(read_input(3))
    jolt_selector.print_solution()


if __name__ == "__main__":
    main()

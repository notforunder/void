import sys
from itertools import *

class Combiner():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_file(self):
        with open(self.input_file, 'r') as f:
            return f.read().splitlines()

    def combine(self):
        collected_lines = self.read_file()
        collected_lines_length = len(collected_lines)
        max = 1 + collected_lines_length
        with open(self.output_file, 'w') as f:
            for min in range(max):
                for i in permutations(collected_lines, min):
                    f.write(' '.join(str(s) for s in i) + '\n')
        print("Successfully combined")


def main():
    combiner = Combiner(sys.argv[1], sys.argv[2])
    combiner.combine()


if __name__ == '__main__':
    main()

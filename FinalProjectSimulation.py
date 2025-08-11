import sys
import math
import os
from multiprocessing import Pool

SYMBOL_TO_VALUE = {'.': 0, 'O': 1, 'o': 2, 'X': 3, 'x': 4}
VALUE_TO_SYMBOL = {0: '.', 1: 'O', 2: 'o', 3: 'X', 4: 'x'}
NEIGHBOR_VALUE = {0: 0, 1: 3, 2: 1, 3: -3, 4: -1}

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def read_matrix(file_path):
    if not os.path.isfile(file_path):
        sys.exit(1)
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        if not lines:
            sys.exit(1)
        matrix = []
        cols = len(lines[0])
        for line in lines:
            if len(line) != cols:
                sys.exit(1)
            row = []
            for c in line:
                if c not in SYMBOL_TO_VALUE:
                    sys.exit(1)
                row.append(SYMBOL_TO_VALUE[c])
            matrix.append(row)
    return matrix

def count_neighbor_values(matrix, row, col, rows, cols):
    neigh_count_sum = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = (row + dr) % rows
            c = (col + dc) % cols
            neigh_count_sum += NEIGHBOR_VALUE[matrix[r][c]]
    return neigh_count_sum

def process_rows(args):
    matrix, start_row, end_row, rows, cols = args
    result = []
    for r in range(start_row, end_row):
        row = []
        for c in range(cols):
            current_cell = matrix[r][c]
            neigh_count_sum = count_neighbor_values(matrix, r, c, rows, cols)
            if current_cell == 1:  # O
                if is_fibonacci(neigh_count_sum):
                    row.append(0)
                elif neigh_count_sum < 12:
                    row.append(2)
                else:
                    row.append(1)
            elif current_cell == 2:  # o
                if neigh_count_sum < 0:
                    row.append(0)
                elif neigh_count_sum > 6:
                    row.append(1)
                else:
                    row.append(2)
            elif current_cell == 0:  # .
                if neigh_count_sum > 0 and is_power_of_two(neigh_count_sum):
                    row.append(2)
                elif neigh_count_sum < 0 and is_power_of_two(abs(neigh_count_sum)):
                    row.append(4)
                else:
                    row.append(0)
            elif current_cell == 3:  # X
                if is_prime(abs(neigh_count_sum)):
                    row.append(0)
                elif neigh_count_sum > -12:
                    row.append(4)
                else:
                    row.append(3)
            elif current_cell == 4:  # x
                if neigh_count_sum >= 1:
                    row.append(0)
                elif neigh_count_sum < -6:
                    row.append(3)
                else:
                    row.append(4)
        result.append(row)
    return result

def next_generation(matrix, process_count):
    rows, cols = len(matrix), len(matrix[0])
    chunk_size = (rows + process_count - 1) // process_count
    tasks = [(matrix, i, min(i + chunk_size, rows), rows, cols) for i in range(0, rows, chunk_size)]
    with Pool(process_count) as pool:
        results = pool.map(process_rows, tasks)
    return [row for chunk in results for row in chunk]

def write_matrix(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(''.join(VALUE_TO_SYMBOL[cell] for cell in row) + '\n')

def simulate(matrix, iterations, output_file, num_processes):
    current_matrix = matrix
    for _ in range(iterations):
        current_matrix = next_generation(current_matrix, num_processes)
    write_matrix(current_matrix, output_file)

def main():
    print("Project :: RNUMBER")
    if len(sys.argv) < 5 or '-i' not in sys.argv or '-o' not in sys.argv:
        sys.exit(1)

    try:
        input_index = sys.argv.index('-i') + 1
        output_index = sys.argv.index('-o') + 1
        input_file = sys.argv[input_index]
        output_file = sys.argv[output_index]
    except (ValueError, IndexError):
        sys.exit(1)

    output_dir = os.path.dirname(output_file) or '.'
    if not os.path.isdir(output_dir):
        sys.exit(1)

    try:
        p_index = sys.argv.index('-p') + 1
        process_count = int(sys.argv[p_index])
        if process_count <= 0:
            sys.exit(1)
    except (ValueError, IndexError):
        process_count = 1

    try:
        matrix = read_matrix(input_file)
        simulate(matrix, 100, output_file, process_count)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()

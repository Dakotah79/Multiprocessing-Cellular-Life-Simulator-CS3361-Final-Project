# Multiprocessing-Cellular-Life-Simulator-CS3361-Final-Project
Parallelized Python cellular automata simulation for CS3361 Final Project – runs 100 iterations with toroidal wrapping, numeric sequence rules, and multiprocessing support.
Multiprocessing Cellular Life Simulator – CS3361 Final Project
Overview

This project is a Python-based parallelized cellular life simulator built for CS3361 – Project #3 (Final Project) at Texas Tech University.
It processes a grid-based simulation over 100 iterations following a set of deterministic rules for different cell types, using Python’s multiprocessing module to improve performance.

The simulator can run in serial mode (default) or parallel mode with a user-specified number of processes.
Features

    Cellular Automata Simulation
    Runs 100 iterations of a custom life simulation with:

        Healthy O cells (O)

        Healthy X cells (X)

        Weakened O cells (o)

        Weakened X cells (x)

        Dead cells (.)

    Custom Update Rules
    Cell state transitions based on neighbor sums, Fibonacci numbers, powers of two, and prime numbers.

    Toroidal Wrapping
    All cells have exactly 8 neighbors; edges wrap around like a donut.

    Parallel Processing
    Uses Python’s built-in multiprocessing module to split work across multiple processes (-p).

    Command-Line Interface
    Clean argument parsing with input/output file control.

Command-Line Usage

python3 <FirstName>_<LastName>_<R#>_final_project.py -i <input_file> -o <output_file> [-p <process_count>]

Arguments
Flag	Required	Description
-i <path>	Yes	Path to input file containing starting matrix
-o <path>	Yes	Path to output file for final matrix after 100 iterations
-p <int>	No	Number of processes to use (default: 1)
Examples

# Run in parallel with 36 processes
python3 Dakota_Hawkins_RNUMBER_final_project.py -i input.txt -o output.txt -p 36

# Run in serial mode
python3 Dakota_Hawkins_RNUMBER_final_project.py -i input.txt -o output.txt

Input File Specification

    ASCII text file

    Symbols:

        O – Healthy O cell

        o – Weakened O cell

        X – Healthy X cell

        x – Weakened X cell

        . – Dead cell

    No spaces or delimiters between symbols

    Each row on its own line

    All rows must have the same length

Example:

..Oo..
O.....
...x..
....O.
....X.
.O..x.

Output File Specification

    Matches input file format

    Contains matrix at time step 100

Project Output

When run, the first line printed will be:

Project :: RNUMBER ID

The simulation then runs silently, writing the final matrix to the output file.
Requirements

    Python 3.x (tested on 3.13.2)

    Standard library only – no external packages (numpy, etc. not allowed)

Development Notes

    Phase 1: Serial computation of matrix updates

    Phase 2: Parallel computation using multiprocessing

    Matrix updates performed on a copy to avoid mid-iteration interference

    Numeric sequences (Fibonacci, powers of two, prime) precomputed for speed

Author

Dakota Hawkins
CS3361 – Spring 2025 – Texas Tech University

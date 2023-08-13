# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework6
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
Sudoku puzzle solver implementation

q1:  Basic Backtracking Search
q2:  Backtracking Search with AC-3
q3:  Backtracking Search with MRV Ordering and AC-3
"""
import csp

# Enter your helper functions here
def constraint(var1, val1, var2, val2):
    return val1 != val2

def build_csp(puzzle):
    """
    Create a Csp object representing the puzzle.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: Csp object
    """
    # Enter your code here and remove the pass statement below
    dictForCSP = {}
    for i in range(9):
        for j in range(9):
            if not (i, j) in puzzle:
                dictForCSP[(i, j)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                dictForCSP[(i, j)] = {puzzle[(i, j)]}

    neighborsForCSP = {}
    for i in range(9):
        for j in range(9):
            neighborsForCSP[(i, j)] = set()

            # add each element as a constraint

            #first 3x3 grid elements
            for k in range(3):
                for l in range(3):

                    #get every element in the corresponding 3x3 sudoku grid area for each variable
                    connectedVar = ((i // 3) * 3 + k, (j // 3) * 3 + l);
                    if connectedVar != (i, j):
                        neighborsForCSP[(i, j)].add(connectedVar)

            #next row elements
            for k in range(9):
                if not (i, j) == (k, j) and not (k, j) in neighborsForCSP[(i, j)]:
                    neighborsForCSP[(i, j)].add((k, j))

            #next column elements
            for k in range(9):
                if not (i, j) == (i, k) and not (i, k) in neighborsForCSP[(i, j)]:
                    neighborsForCSP[(i, j)].add((i, k))

    return csp.Csp(dictForCSP, neighborsForCSP, constraint)


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    cspForQ1 = build_csp(puzzle)
    return (cspForQ1.backtracking_search(), cspForQ1)


def q2(puzzle):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    cspForQ1 = build_csp(puzzle)
    cspForQ1.ac3_algorithm()
    return (cspForQ1.backtracking_search(), cspForQ1)


def q3(puzzle):
    """
    Solve the given puzzle with backtracking search and MRV ordering and
    AC-3 as a preprocessing step.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    cspForQ1 = build_csp(puzzle)
    cspForQ1.ac3_algorithm()
    return (cspForQ1.backtracking_search("MRV"), cspForQ1)
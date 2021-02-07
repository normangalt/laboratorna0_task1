'''
Skyscrapers.py

GITHUB repository link:https://github.com/normangalt/laboratorna0_task1
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    """
    with open(path, 'r', encoding = 'utf-8') as file:
        content = file.readlines()
        content = [line[:-1] for line in content[:-1]] + [content[-1]]
        return content

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    number = 1
    max_element = input_line[1]
    for index in range(2, len(input_line) - 1):
        curr_element = input_line[index]
        if curr_element > max_element:
            max_element = curr_element
            number += 1

    if pivot != '*':
        return number == int(pivot)

    return True

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
                                  '*?????5', '*?????*', '*?????*',\
                                  '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for line in board:
        for element in line:
            if element == '?':
                return False
    return True

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for line in board[1:-1]:
        updated_line = line[1:-1]
        for element in updated_line:

            number = updated_line.count(element)
            if number > 1:
                return False

    return True

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for line in board[1:-1]:
        if not left_to_right_check(line, line[0]) or \
           not left_to_right_check(list(reversed(line)), line[-1]):
            return False

    return True

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function
    for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """

    transposed_board = [[board[jindex][index] for jindex in range(len(board))]
                        for index in range(len(board[0]))]

    if check_uniqueness_in_rows(transposed_board) and \
       check_not_finished_board(transposed_board) and \
       check_horizontal_visibility(transposed_board):
        return True

    return False

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """
    board = read_input(input_path)
    if check_uniqueness_in_rows(board) and \
       check_not_finished_board(board) and \
       check_horizontal_visibility(board):
        return check_columns(board)
    return False

import doctest
doctest.testmod()
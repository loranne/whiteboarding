#!/usr/bin/python

def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":

    >>> check("D6", "H6")
    True
    >>> check("E6", "E4")
    True
    >>> check("B7", "D5")
    True
    >>> check("A1", "H8")
    True
    >>> check("A8", "H1")
    True
    >>> check("D6", "H7")
    False
    >>> check("E6", "F4")
    False

    """

    # easily determine if K and Q share a row or a column if the row coordinates match OR if the column coordinates match
    # so, if coordinates have the same letter or the same number, then it evaluates to true
    # no need to worry about K and Q sharing both the letter and the number
    # index into string at a given position, and see if that position is equal for K and Q
    # if yes, return true
    # if king[0] = queen[0] + 1
    # need to be able to count letters
    # want to calculate the difference between K and Q coordinates. If the difference looks something like
    # -1, 1 or -2, 2
    # array of letters for the board, then I can make the letters correspond to ints
    # and it's easier to calculate differences

    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # if row or coloumn is the same, return true
    if king[0] == queen[0] or king[1] == queen[1]:
        return True
    
    row_diff = abs(int(king[1]) - int(queen[1]))

    # 2 for loops using enumerate to find indices of king and queen letters
    # for idx_queen, letter in enumerate(cols):
    #     idx_queen = queen[0]

    # for idx_king, letter in enumerate(cols):
    #     idx_king = king[0]
        # print(type(idx_king))
        # print(idx_king) 

    # remember your .index method!!!!
    idx_king = cols.index(king[0])

    idx_queen = cols.index(queen[0])

    col_diff = abs(int(idx_king) - int(idx_queen))

    if col_diff == row_diff:
        return True
    
    return False


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GREAT JOB!")
    print()

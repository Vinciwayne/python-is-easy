
"""
 Advanced Loops
"""




def create_board(rows, columns):
    max_columns = 130
    max_rows = 11
    rows = int(rows)
    columns = int(columns)
    if columns <= max_columns and rows <= max_rows:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        # After drawing is done return True
        return True
    else:
        # Return False when matrix is not fitting the screen
        reason = ""
        if columns > max_columns and rows > max_rows:
            reason = "columns and rows"
        elif columns > max_columns:
            reason += "columns"
        elif rows > max_rows:
            reason += "rows"
        print("Sorry, cannot create the board, too many {0:s}.".format(reason))
        return False


create_board(11, 130)






"""

EZEBUIRO UCHECHUKWU VINCENT

"""
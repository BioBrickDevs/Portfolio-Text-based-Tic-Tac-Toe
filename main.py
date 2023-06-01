from replit import clear
from pynput import keyboard
import os


def main_game():
    clear()
    board = """
            __|__|__
            __|__|__
              |  |
            """

    a1 = "___|"
    b1 = "___"
    c1 = "|___"
    a2 = "___|"
    b2 = "___"
    c2 = "|___"
    a3 = "   |"
    b3 = "   "
    c3 = "|  "

    global cursor
    global dublicate
    global last_symbol
    global how_many_marks
    how_many_marks = 0
    last_symbol = "::"
    cursor = "::"
    dublicate = False
    global end_game
    end_game = False
    row1 = [a1, b1, c1]
    row2 = [a2, b2, c2]
    row3 = [a3, b3, c3]
    rows = [row1, row2, row3]

    def display_grid(grid):
        for x, row in enumerate(rows):
            row_to_display = ""
            for y, symbol in enumerate(row):
                row_to_display += symbol
            print(row_to_display)

    def display_cursor_at_grid_pos(grid, cordx, cordy):
        global last_symbol
        global cursor
        for x, row in enumerate(rows):
            row_to_display = ""
            for y, symbol in enumerate(row):
                if cordx == x and cordy == y:
                    symbol = list(symbol)
                    symbol[1] = last_symbol
                    symbol = "".join(symbol)
                    row_to_display += symbol
                else:
                    row_to_display += symbol
            print(row_to_display)

    def paint_cursor(grid, cordx, cordy):
        global cursor
        global dublicate
        for x, row in enumerate(rows):
            row_to_display = ""
            for y, symbol in enumerate(row):
                if cordx == x and cordy == y:
                    symbol = list(symbol)
                    symbol[1] = cursor
                    symbol = "".join(symbol)
                    row_to_display += symbol
                    to_check_for = rows[x][y]
                    if "0" in to_check_for or "X" in to_check_for:
                        dublicate = True

                    else:
                        rows[x][y] = symbol
                        dublicate = False
                else:
                    row_to_display += symbol
            print(row_to_display)

    def move_down():
        global y
        if y + 1 > 2:
            pass
        else:
            y += 1
        clear()
        display_cursor_at_grid_pos(rows, y, x)

    def move_up():
        global y
        if y - 1 < 0:
            pass
        else:
            y -= 1
        clear()
        display_cursor_at_grid_pos(rows, y, x)

    global x
    global y
    x = 0
    y = 0

    def move_right():
        global x
        if x + 1 > 2:
            pass
        else:
            x += 1
        clear()
        display_cursor_at_grid_pos(rows, y, x)

    def move_left():
        global x
        if x - 1 < 0:
            pass
        else:
            x -= 1
        clear()
        display_cursor_at_grid_pos(rows, y, x)

    def check_for_win(grid):
        for rows in grid:
            three_straight_X = 0
            three_straight_0 = 0

            for row in rows:
                if "X" in row:
                    three_straight_X += 1
                if "0" in row:
                    three_straight_0 += 1

                if three_straight_X == 3:
                    return 1
                elif three_straight_0 == 3:
                    return 0
                else:
                    pass
        column = 0
        row = 0

        while column <= 2:
            row = 0
            three_straight_0 = 0
            three_straight_X = 0
            while row <= 2:
                if "X" in grid[row][column]:

                    three_straight_X += 1
                if "0" in grid[row][column]:

                    three_straight_0 += 1

                if three_straight_X == 3:
                    return 1

                elif three_straight_0 == 3:
                    return 0

                else:
                    pass

                row += 1
            column += 1

        three_straight_0 = 0
        three_straight_X = 0

        for number in range(3):
            if "X" in grid[number][number]:
                three_straight_X += 1

            if "0" in grid[number][number]:
                three_straight_0 += 1

            if three_straight_X == 3:
                return 1

            elif three_straight_0 == 3:
                return 0

            else:
                pass

        three_straight_0 = 0
        three_straight_X = 0

        for result in range(3):

            if "X" in grid[result][2 - result]:
                three_straight_X += 1

            if "0" in grid[result][2 - result]:
                three_straight_0 += 1

            if three_straight_X == 3:
                return 1

            elif three_straight_0 == 3:
                return 0
            else:
                pass

    def mark():
        global how_many_marks
        global last_symbol
        global cursor
        global dublicate
        if dublicate:
            pass
        else:
            how_many_marks += 1
            if cursor == "::":

                last_symbol = "::"

                cursor = "X"

            elif cursor == "X":

                last_symbol = "::"

                cursor = "0"

            else:

                last_symbol = "::"

                cursor = "X"

        clear()
        display_cursor_at_grid_pos(rows, y, x)
        clear()
        paint_cursor(rows, y, x)

    global n_pressed
    n_pressed = False

    def on_press(key):
        global end_game
        global n_pressed
        global how_many_marks

        if end_game or how_many_marks == 9:
            if key == keyboard.KeyCode.from_char("y"):
                main_game()

            elif key == keyboard.KeyCode.from_char("n"):
                n_pressed = True

        else:
            if key == key.up:
                move_up()
            if key == key.down:
                move_down()
            if key == key.left:
                move_left()
            if key == key.right:
                move_right()
            if key == key.space:
                mark()
            if check_for_win(grid=rows) == 1:
                print("X won")
                print("Do you want to play again?(Y/N)")
                end_game = True
            elif check_for_win(grid=rows) == 0:
                print("0 won")
                print("Do you want to play again?(Y/N)")
                end_game = True
            elif how_many_marks == 9:
                print("Game is even.")
                print("Do you want to play again?(Y/N)")

    def on_release(key):
        global n_pressed
        if n_pressed is True:
            os._exit(0)

    print("Start by moving the cursor with arrows.")
    print("Press space for mark.")
    display_grid(rows)

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


main_game()

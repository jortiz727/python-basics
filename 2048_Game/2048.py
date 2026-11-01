from shutil import move

import logic

def print_board(mat):
    for row in mat:
        line = ""
        for cell in row:
            line += f"{cell:5}"
        print(line)
    print()

if __name__ == '__main__':
    mat = logic.start_game()

    while(True):
        x = input("Press the command : ").lower()
        #quit game
        if x == 'q':
            print("Game Terminated")
            break

        #move to up
        elif x == 'w':
            mat, flag = logic.move_up(mat)
            status = logic.get_current_state(mat)
            print_board(mat)
            print(status)

            if(status == 'GAME NOT OVER'):
                logic.add_new_2(mat)
            else:
                break

        #move to down
        elif x == 's':
            mat, flag = logic.move_down(mat)
            status = logic.get_current_state(mat)
            print_board(mat)
            print(status)

            if(status == 'GAME NOT OVER'):
                logic.add_new_2(mat)
            else:
                break

        #move to the left
        elif x == 'a':
            mat, flag = logic.move_left(mat)
            status = logic.get_current_state(mat)
            print_board(mat)
            print(status)

            if(status == 'GAME NOT OVER'):
                logic.add_new_2(mat)
            else:
                break

        #move to the right
        elif x == 'd':
            mat, flag = logic.move_right(mat)
            status = logic.get_current_state(mat)
            print_board(mat)
            print(status)

            if(status == 'GAME NOT OVER'):
                logic.add_new_2(mat)
            else:
                break

        else:
            print("Invalid Key Pressed")
            continue

        mat, flag = move(mat)
        if flag:
            logic.add_new_2(mat)

        print_board(mat)

        status = logic.get_current_state(mat)
    
        if status == 'WON':
            print("You reached 2048! You win!")
            break
        elif status == 'LOST':
            print("GAME OVER - no moves left.")
            break

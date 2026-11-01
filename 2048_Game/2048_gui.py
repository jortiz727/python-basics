import tkinter as tk

import logic

TEXT_COLOR = "#ffffff"
TILE_COLORS = {
    0: "#cbc9c6",
    2: "#fcc287",
    4: "#ffa600",
    8: "#ff7700",
    16: "#ff5900",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#ffbf00",
    256: "#ea00ff",
    512: "#ff0062",
    1024: "#dd00ff",
    2048: "#00ff1e",
}


def draw_board():
    for r in range(4):
        for c in range(4):
            value = mat[r][c]
            if value == 0:
                text = ""
            else:
                text = str(value)
            labels[r][c].config(text=text, bg=TILE_COLORS[value])


def on_key(event):
    global mat
    key = event.keysym.lower()

    if key in ("w", "up"):
        move = logic.move_up
    elif key in ("s", "down"):
        move = logic.move_down
    elif key in ("a", "left"):
        move = logic.move_left
    elif key in ("d", "right"):
        move = logic.move_right
    else:
        return

    mat, flag = move(mat)

    if flag:
        logic.add_new_2(mat)

    draw_board()

    status = logic.get_current_state(mat)
    if status == 'WON':
        status_label.config(text="You reached 2048! You win!")
        window.unbind("<Key>")
    elif status == 'LOST':
        status_label.config(text="GAME OVER - no moves left.")
        window.unbind("<Key>")


window = tk.Tk()
window.title("2048")

board = tk.Frame(window, bg="#bbada0", padx=5, pady=5)
board.pack(padx=10, pady=10)

labels = []
for r in range(4):
    row = []
    for c in range(4):
        label = tk.Label(board, width=4, height=2,
                         font=("Arial", 24, "bold"), fg=TEXT_COLOR)
        label.grid(row=r, column=c, padx=5, pady=5)
        row.append(label)
    labels.append(row)

status_label = tk.Label(window, text="Use WASD or the arrow keys",
                        font=("Arial", 14))
status_label.pack(pady=(0, 10))

mat = logic.start_game()
draw_board()

window.bind("<Key>", on_key)
window.mainloop()

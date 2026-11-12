import random
import string
import tkinter

wid = 600
hiy = 400


def genblock():
    digits = random.choices(string.digits, k=2)
    letters = random.choices(string.ascii_uppercase, k=3)
    block = digits + letters
    random.shuffle(block)
    return "".join(block)


def genkey():
    blocks = []
    for i in range(3):
        blocks.append(genblock())
    return "-".join(blocks)


def on_generate():
    key_var.set(genkey())


root = tkinter.Tk()
root.title("KeyGen - вариант 1")

canvas = tkinter.Canvas(root, width=wid, height=hiy)
canvas.pack()

bg_image = tkinter.PhotoImage(file="SC2.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

canvas.create_text(wid // 2 + 2, 257, text="KEY GENERATOR", fill="black",
                   font=("Courier New", 20, "bold"))
canvas.create_text(wid // 2, 255, text="KEY GENERATOR", fill="#7fd4ff",
                   font=("Courier New", 20, "bold"))

key_var = tkinter.StringVar(value="XXXXX-XXXXX-XXXXX")
key_entry = tkinter.Entry(root, textvariable=key_var, font=("Courier New", 22),
                          justify="center", width=19, state="readonly")
canvas.create_window(wid // 2, 305, window=key_entry)

button = tkinter.Button(root, text="Сгенерировать", font=("Arial", 14),
                        command=on_generate)
canvas.create_window(wid // 2, 360, window=button)

root.mainloop()

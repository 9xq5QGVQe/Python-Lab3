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


def bindgen():
    keyn.set(genkey())


root = tkinter.Tk()
root.title("KeyGen - вариант 1")

back = tkinter.Canvas(root, width = wid, height = hiy)
back.pack()

png = tkinter.PhotoImage(file="SC2.png")
back.create_image(0, 0, image = png, anchor = "nw")

back.create_text(wid // 2 + 2, 257, text = "KEY GENERATOR", fill = "black",
                   font = ("Courier New", 20, "bold"))
back.create_text(wid // 2, 255, text="KEY GENERATOR", fill = "#7fd4ff",
                   font = ("Courier New", 20, "bold"))

keyn = tkinter.StringVar(value="XXXXX-XXXXX-XXXXX")
keye = tkinter.Entry(root, textvariable = keyn, font = ("Courier New", 22),
                          justify = "center", width = 19, state = "readonly")
back.create_window(wid // 2, 305, window = keye)

but = tkinter.Button(root, text="Сгенерировать", font = ("Arial", 14),
                        command = bindgen)
back.create_window(wid // 2, 360, window = but)

root.mainloop()

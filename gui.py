from pathlib import Path
from tkinter import Tk, Canvas, Label, Button, PhotoImage

    
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("492x669+150+15")
window.configure(bg = "#CACACA")
window.iconbitmap(relative_to_assets("robozinho.ico"))
window.title("Automação E2DOC")


canvas = Canvas(
    window,
    bg = "#CACACA",
    height = 669,
    width = 492,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    246.0,
    334.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=45.0,
    y=79.74510192871094,
    width=301.1538391113281,
    height=31.372549057006836
)

canvas.create_text(
    45.0,
    57.0,
    anchor="nw",
    text="FÉRIAS",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    46.0,
    268.0,
    anchor="nw",
    text="PAGTOS MANUAIS",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    45.0,
    338.0,
    anchor="nw",
    text="REMESSA ITAÚ",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    45.0,
    198.0,
    anchor="nw",
    text="13º SALÁRIO",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    46.0,
    128.0,
    anchor="nw",
    text="RECISÕES",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=46.0,
    y=150.39215087890625,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=45.0,
    y=221.03921508789062,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    cursor="hand2"
)
button_4.place(
    x=46.0,
    y=290.686279296875,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    cursor="hand2"
)
button_5.place(
    x=46.0,
    y=361.0,
    width=301.1538391113281,
    height=31.372549057006836
)

canvas.create_text(
    46.0,
    408.0,
    anchor="nw",
    text="PAGTOS DE VA e VT",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    46.0,
    479.0,
    anchor="nw",
    text="LOCAÇÃO FROTA",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    cursor="hand2"
)
button_6.place(
    x=46.0,
    y=430.9803771972656,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    cursor="hand2"
)
button_7.place(
    x=46.0,
    y=501.62744140625,
    width=301.1538391113281,
    height=31.372549057006836
)

entry_1 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_1.place(
    x=369.0,
    y=80.0,
    width=98.0,
    height=29.0
)

entry_2 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_2.place(
    x=370.0,
    y=150.0,
    width=98.0,
    height=30.0
)

entry_3 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_3.place(
    x=369.0,
    y=221.0,
    width=98.0,
    height=29.0
)

entry_4 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_4.place(
    x=370.0,
    y=291.0,
    width=98.0,
    height=29.0
)

entry_5 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_5.place(
    x=370.0,
    y=360.0,
    width=98.0,
    height=30.0
)

entry_6 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_6.place(
    x=370.0,
    y=431.0,
    width=98.0,
    height=29.0
)

entry_7 = Label(
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888"
)
entry_7.place(
    x=370.0,
    y=502.0,
    width=98.0,
    height=29.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    cursor="hand2"
)
button_8.place(
    x=107.0,
    y=566.0,
    width=278.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()

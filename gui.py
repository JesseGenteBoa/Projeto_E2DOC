from pathlib import Path
from tkinter import Tk, Canvas, Label, Button, PhotoImage, messagebox, StringVar
from tkinter.filedialog import askdirectory
import utils

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build\assets\frame0")

lista_de_pastas = []


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def selecionar_pasta(tipo):
    global pasta_comprovante, label_fgts, label_ferias, label_rescisao, label_13, lista_de_pastas
    global label_remessa_itau, label_locacao_frota, label_pagtos_manuais, label_pagtosVAVT

    pasta_comprovante = askdirectory(title="Selecione a pasta com os comprovantes que deseja enviar.")
    match tipo:
        case "FÉRIAS":
            utils.adicionar_pasta(pasta_comprovante, "FERIAS", label_ferias, lista_de_pastas)
        case "RESCISÕES":
            utils.adicionar_pasta(pasta_comprovante, "RESCISOES", label_rescisao, lista_de_pastas)
        case "13º SALÁRIO":
            utils.adicionar_pasta(pasta_comprovante, "13 SALARIO", label_13, lista_de_pastas)
        case "REMESSA ITAÚ":
            utils.adicionar_pasta(pasta_comprovante, "REMESSA ITAU", label_remessa_itau, lista_de_pastas)
        case "LOCAÇÃO FROTA":
            utils.adicionar_pasta(pasta_comprovante, "LOCAÇÃO VEICULO", label_locacao_frota, lista_de_pastas)
    print(lista_de_pastas)



window = Tk()

window.geometry("492x669+150+15")
window.configure(bg = "#CACACA")
window.iconbitmap(relative_to_assets("robozinho.ico"))
window.title("Automação E2DOC")


label_fgts = StringVar()
label_ferias = StringVar()
label_rescisao = StringVar()
label_13 = StringVar()
label_remessa_itau = StringVar()
label_locacao_frota = StringVar()
label_pagtos_manuais = StringVar()
label_pagtosVAVT = StringVar()


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
    x=43.0,
    y=72.0,
    width=301.1538391113281,
    height=31.372549057006836
)

canvas.create_text(
    43.0,
    50.0,
    anchor="nw",
    text="FGTS",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    242.0,
    anchor="nw",
    text="13º SALÁRIO",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    306.0,
    anchor="nw",
    text="REMESSA ITAÚ",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    178.0,
    anchor="nw",
    text="RESCISÃO",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    114.0,
    anchor="nw",
    text="FÉRIAS",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(tipo="FÉRIAS"),
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=43.0,
    y=136.49014282226562,
    width=301.1538391113281,
    height=31.09849548339844
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(tipo="RESCISÕES"),
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=43.0,
    y=200.0,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(tipo="13º SALÁRIO"),
    relief="flat",
    cursor="hand2"
)
button_4.place(
    x=43.0,
    y=263.686279296875,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(tipo="REMESSA ITAÚ"),
    relief="flat",
    cursor="hand2"
)
button_5.place(
    x=43.0,
    y=328.0,
    width=301.1538391113281,
    height=31.372549057006836
)

canvas.create_text(
    44.0,
    372.0,
    anchor="nw",
    text="LOCAÇÃO FROTA",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    436.0,
    anchor="nw",
    text="PAGTOS MANUAIS",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

canvas.create_text(
    43.0,
    503.0,
    anchor="nw",
    text="PAGTOS DE VA e VT",
    fill="#000000",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_pasta(tipo="LOCAÇÃO FROTA"),
    relief="flat",
    cursor="hand2"
)
button_6.place(
    x=43.0,
    y=394.0,
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
    x=43.0,
    y=458.0,
    width=301.1538391113281,
    height=31.372549057006836
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    cursor="hand2"
)
button_8.place(
    x=43.0,
    y=525.0,
    width=301.1538391113281,
    height=31.372549057006836
)

entry_1 = Label(
    textvariable=label_fgts,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_1.place(
    x=368.0,
    y=72.0,
    width=98.0,
    height=29.0
)

entry_2 = Label(
    textvariable=label_ferias,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_2.place(
    x=368.0,
    y=136.0,
    width=98.0,
    height=30.0
)

entry_3 = Label(
    textvariable=label_rescisao,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_3.place(
    x=368.0,
    y=200.0,
    width=98.0,
    height=29.0
)

entry_4 = Label(
    textvariable=label_13,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 11 * -1)
)
entry_4.place(
    x=368.0,
    y=263.0,
    width=98.0,
    height=29.0
)

entry_5 = Label(
    textvariable=label_remessa_itau,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_5.place(
    x=368.0,
    y=327.0,
    width=98.0,
    height=30.0
)

entry_6 = Label(
    textvariable=label_locacao_frota,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_6.place(
    x=368.0,
    y=394.0,
    width=98.0,
    height=29.0
)

entry_7 = Label(
    textvariable=label_pagtos_manuais,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_7.place(
    x=368.0,
    y=458.0,
    width=98.0,
    height=29.0
)

entry_8 = Label(
    textvariable=label_pagtosVAVT,
    bd=0,
    bg="#CACACA",
    fg="#000716",
    highlightthickness=0.5,
    highlightbackground="#888888",
    font=("Bahnschrift SemiLight SemiConde", 16 * -1)
)
entry_8.place(
    x=368.0,
    y=525.0,
    width=98.0,
    height=29.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    cursor="hand2"
)
button_9.place(
    x=107.0,
    y=578.0,
    width=278.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()



 

import threading
from time import sleep
from pathlib import Path
from tkinter.filedialog import askopenfilenames
from tkinter import Tk, Canvas, Label, Button, PhotoImage, StringVar

arquivos = []

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Projeto E2DOC\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def selecionar_arquivo():
    global caminho_arq_comprovante, arquivos, label_arquivo
    caminho_arq_comprovante = askopenfilenames(title="Selecione o arquivo de comprovantes.", filetypes=[("PDF Files", "*.pdf")])
    verificacao = [arq for arq in caminho_arq_comprovante if arq not in arquivos]
    arquivos = arquivos + verificacao
    label_arquivo.set("   ".join(arquivos[-1].split('/')[-3:]).split('.')[0])
    threading.Thread(target=atualizar_label, args=(arquivos,)).start()


def atualizar_label(arquivos):
    sleep(7)
    for arq in arquivos:
        label_arquivo.set("   ".join(arq.split('/')[-3:]).split('.')[0])
        sleep(7)


window = Tk()

window.geometry("587x381+150+30")
window.configure(bg = "#CACACA")
window.iconbitmap(relative_to_assets("robozinho.ico"))
window.title("Automação E2DOC")

label_arquivo = StringVar()

canvas = Canvas(
    window,
    bg = "#CACACA",
    height = 381,
    width = 588,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = -0.5, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    294.0,
    191.0,
    image=image_image_1
)

entry_1 = Label(
    textvariable=label_arquivo,
    bd=0,
    bg="#DEDEDE",
    fg="#000716",
    highlightthickness=2.3,
    highlightbackground="#525252",
    font=("Bahnschrift SemiLight SemiConde", 18 * -1)
)
entry_1.place(
    x=62.0,
    y=87.0,
    width=388.0,
    height=48.0
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
    x=475.0,
    y=87.0,
    width=50.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    cursor="hand2"
)
button_2.place(
    x=154.0,
    y=272.0,
    width=278.0,
    height=66.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_arquivo(),
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=60.0,
    y=167.0,
    width=468.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()

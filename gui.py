import queue
import threading
import tkinter as tk
from time import sleep
from pathlib import Path
from utils import zerar_lista_controle
from tkinter.filedialog import askopenfilenames


arquivos = []
lista_controle = queue.Queue()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Projeto E2DOC\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def modificar_lista():
    global arquivos, lista_controle
    lista = [" \\ ".join(item.split('/')[-3:]).split('.')[0] for item in arquivos]

    def excluir_itens():
        selecionados = listbox.curselection()
        for i in reversed(selecionados):
            listbox.delete(i)
            del arquivos[i]
        try:
            label_arquivo.set("   ".join(arquivos[0].split('/')[-3:]).split('.')[0])
            zerar_lista_controle(lista_controle)
            lista_controle.put(1)
        except IndexError:
            zerar_lista_controle(lista_controle)
            label_arquivo.set("")

    root = tk.Tk()
    root.geometry("330x310+80+80")
    root.iconbitmap(relative_to_assets("robozinho.ico"))
    root.configure(bg = "#CACACA")
    root.title("Lista de Arquivos")

    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Bahnschrift SemiLight SemiConde", 16 * -1), justify=tk.CENTER)
    listbox.pack(ipadx=80, ipady=10, padx=10, pady=10)

    for item in lista:
        listbox.insert(tk.END, item)

    btn_excluir = tk.Button(root, text="Excluir Selecionados", cursor="hand2", justify="center", font=("Bahnschrift SemiLight SemiConde", 17 * -1), command=excluir_itens)
    btn_excluir.pack(fill=tk.Y, pady=10, ipadx=10, ipady=2)

    root.mainloop()



def selecionar_arquivo():
    global caminho_arq_comprovante, arquivos, label_arquivo, lista_controle
    caminho_arq_comprovante = askopenfilenames(title="Selecione o arquivo de comprovantes.", filetypes=[("PDF Files", "*.pdf")])
    verificacao = [arq for arq in caminho_arq_comprovante if arq not in arquivos]
    arquivos = arquivos + verificacao
    label_arquivo.set("   ".join(arquivos[-1].split('/')[-3:]).split('.')[0])
    lista_controle.put(1)
    if lista_controle.qsize() == 1:
        threading.Thread(target=atualizar_label).start()



def atualizar_label():
    global arquivos
    sleep(5)
    if len(arquivos) > 0:
        for arq in arquivos:
            if lista_controle.qsize() == 1:
                label_arquivo.set("   ".join(arq.split('/')[-3:]).split('.')[0])
            else:
                zerar_lista_controle(lista_controle)
                lista_controle.put(1)
            sleep(5)
        return atualizar_label()
    else:
        label_arquivo.set("")



window = tk.Tk()

window.geometry("587x381+412+80")
window.configure(bg = "#CACACA")
window.iconbitmap(relative_to_assets("robozinho.ico"))
window.title("Automação E2DOC")

label_arquivo = tk.StringVar()

canvas = tk.Canvas(
    window,
    bg = "#CACACA",
    height = 381,
    width = 588,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = -0.5, y = 0)
image_image_1 = tk.PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    294.0,
    191.0,
    image=image_image_1
)

entry_1 = tk.Label(
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

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: modificar_lista(),
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=475.0,
    y=87.0,
    width=50.0,
    height=49.0
)

button_image_2 = tk.PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
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

button_image_3 = tk.PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = tk.Button(
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

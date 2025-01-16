import os
import queue
import threading
import docHudson
import tkinter as tk
from time import sleep
from tkinter import ttk
from pathlib import Path
from guiLog import abrir_janela_resultado
from tkinter.filedialog import askopenfilenames
from utils import zerar_lista_controle, retornar_dt_festiva


lista_controle = queue.Queue()
em_execucao = queue.Queue()
janela_aberta = False
arquivos = []


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def executar():
    global em_execucao, arquivos
    em_execucao.put(1)

    try:
        modelos_enviados = docHudson.executar_automacao(arquivos)
    except FileNotFoundError as e:
        tk.messagebox.showerror("Erro!", e)

    feriado = retornar_dt_festiva()

    label_total_geral = tk.IntVar(value=len(modelos_enviados))
    label_proventos = tk.IntVar(value=0)
    label_rescisao = tk.IntVar(value=0)
    label_locacao = tk.IntVar(value=0)
    label_ferias = tk.IntVar(value=0)
    label_fgts = tk.IntVar(value=0)
    label_13 = tk.IntVar(value=0)
    label_vt = tk.IntVar(value=0)
    label_va = tk.IntVar(value=0)
    texto = tk.StringVar()

    for modelo_documento in modelos_enviados:
        match modelo_documento:
            case 'MULTAS DE FGTS RESCISÓRIA':
                label_fgts.set(label_fgts.get() + 1)
            case '13 SALARIO':
                label_13.set(label_13.get() + 1)
            case 'PROVENTOS':
                label_proventos.set(label_proventos.get() + 1)
            case 'RESCISÕES':
                label_rescisao.set(label_rescisao.get() + 1)
            case 'LOCAÇÃO':
                label_locacao.set(label_locacao.get() + 1)
            case 'FÉRIAS':
                label_ferias.set(label_ferias.get() + 1)
            case 'VT':
                label_vt.set(label_vt.get() + 1)
            case 'VA':
                label_va.set(label_va.get() + 1)
                
    texto.set(f'''
Envio finalizado com sucesso!!!

{feriado}

Até a próxima!
''')
    threading.Thread(target=abrir_janela_resultado, args=(window, label_ferias, label_13, label_locacao, label_vt, label_va, label_proventos, label_rescisao, label_fgts, texto, label_total_geral), daemon=True).start()



def acionar_automacao():
    global arquivos, em_execucao
    if em_execucao.qsize() == 0 and arquivos:
        janela_espera = tk.Toplevel(window)
        janela_espera.iconbitmap(relative_to_assets("robozinho.ico"))
        janela_espera.title("Aguarde...")
        janela_espera.geometry("300x130+552+285")

        label_espera = tk.Label(janela_espera, text="Enviando...", font=("Bahnschrift SemiLight SemiConde", 18 * -1))
        label_espera.pack(pady=20)

        progresso = ttk.Progressbar(janela_espera, mode="indeterminate")
        progresso.pack(pady=10, padx=1, ipadx=50)
        progresso.start()

        def _acionar_automacao(em_execucao):
            executar()
            janela_espera.destroy()
            zerar_lista_controle(em_execucao)
            arquivos.clear()
            label_arquivo.set("")
        
        janela_espera.resizable(False, False)

        threading.Thread(target=_acionar_automacao, args=(em_execucao,), daemon=True).start()



def modificar_lista():
    global arquivos, lista_controle, janela_aberta

    if janela_aberta:
        return

    janela_aberta = True

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

    def abrir_pdf():
        selecionados = listbox.curselection()
        if selecionados:
            for index in selecionados:
                caminho_pdf = arquivos[index]
                os.startfile(caminho_pdf)

    def controle_janela():
        global janela_aberta
        janela_aberta = False
        root.destroy()

    root = tk.Tk()
    root.geometry("331x310+80+80")
    root.iconbitmap(relative_to_assets("robozinho.ico"))
    root.configure(bg="#CACACA")
    root.title("Lista de Arquivos")
    root.protocol("WM_DELETE_WINDOW", controle_janela)

    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Bahnschrift SemiLight SemiConde", 16 * -1), justify=tk.CENTER)
    listbox.pack(ipadx=80, ipady=10, padx=10, pady=10)

    for item in lista:
        listbox.insert(tk.END, item)

    frame_buttons = tk.Frame(root, bg="#CACACA")
    frame_buttons.pack(fill=tk.BOTH, pady=10, padx=10)

    btn_excluir = tk.Button(frame_buttons, text="Excluir Selecionados", cursor="hand2", justify="center",
                            font=("Bahnschrift SemiLight SemiConde", 17 * -1), command=excluir_itens)
    btn_excluir.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=15, ipadx=5, ipady=2)

    btn_abrir = tk.Button(frame_buttons, text="Abrir PDF", cursor="hand2", justify="center",
                          font=("Bahnschrift SemiLight SemiConde", 17 * -1), command=abrir_pdf)
    btn_abrir.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=15, ipadx=5, ipady=2)

    root.resizable(False, False)
    root.mainloop()



def selecionar_arquivo():
    global caminho_arq_comprovante, arquivos, label_arquivo, lista_controle
    caminho_arq_comprovante = askopenfilenames(title="Selecione o arquivo com os comprovantes.", filetypes=[("PDF Files", "*.pdf")])
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
    command=lambda: acionar_automacao(),
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

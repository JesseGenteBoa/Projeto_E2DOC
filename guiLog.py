from pathlib import Path
from tkinter import Toplevel, Canvas, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Imagens")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def abrir_janela_resultado(window, label_ferias, label_13, label_locacao, label_vt, label_va, label_proventos, label_rescisao, label_fgts, texto, label_total_geral):

    janela_enviados = Toplevel(window)

    janela_enviados.geometry("607x436+412+80")
    janela_enviados.configure(bg = "#E3E3E3")
    janela_enviados.iconbitmap(relative_to_assets("robozinho.ico"))
    janela_enviados.title("Enviados")

    canvas2 = Canvas(
        janela_enviados,
        bg = "#E3E3E3",
        height = 436,
        width = 607,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas2.place(x = 0, y = 0)

    canvas2.create_text(
        99.0,
        64.0,
        anchor="nw",
        text="FÉRIAS",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        213.0,
        64.0,
        anchor="nw",
        text="RESCISÕES",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        329.0,
        64.0,
        anchor="nw",
        text="13º SALÁRIO",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        473.0,
        64.0,
        anchor="nw",
        text="FGTS",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        235.0,
        123.0,
        anchor="nw",
        text="VT",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        87.0,
        123.0,
        anchor="nw",
        text="PROVENTOS",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        441.0,
        123.0,
        anchor="nw",
        text="LOCAÇÃO FROTA",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        358.0,
        122.0,
        anchor="nw",
        text="VA",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    entry_vt = Label(
        janela_enviados,
        textvariable=label_vt,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_vt.place(
        x=185.0,
        y=144.0,
        width=115.0,
        height=24.0
    )

    entry_va = Label(
        janela_enviados,
        textvariable=label_va,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_va.place(
        x=308.0,
        y=144.0,
        width=115.0,
        height=24.0
    )

    entry_loc = Label(
        janela_enviados,
        textvariable=label_locacao,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_loc.place(
        x=431.0,
        y=144.0,
        width=115.0,
        height=24.0
    )

    entry_fgts = Label(
        janela_enviados,
        textvariable=label_fgts,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_fgts.place(
        x=431.0,
        y=86.0,
        width=115.0,
        height=24.0
    )

    entry_13 = Label(
        janela_enviados,
        textvariable=label_13,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_13.place(
        x=308.0,
        y=86.0,
        width=115.0,
        height=24.0
    )

    entry_total_geral = Label(
        janela_enviados,
        textvariable=label_total_geral,
        bd=0,
        bg="#E3E3E3",
        fg="#000716",
        highlightthickness=0,
        font=("Bahnschrift SemiLight SemiConde", 20 * -1)
    )
    entry_total_geral.place(
        x=500.0,
        y=13.0,
        width=64.0,
        height=24.0
    )

    entry_resc = Label(
        janela_enviados,
        textvariable=label_rescisao,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_resc.place(
        x=185.0,
        y=86.0,
        width=115.0,
        height=24.0
    )

    entry_ferias = Label(
        janela_enviados,
        textvariable=label_ferias,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_ferias.place(
        x=62.0,
        y=86.0,
        width=115.0,
        height=24.0
    )

    entry_prov = Label(
        janela_enviados,
        textvariable=label_proventos,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 15 * -1)
    )
    entry_prov.place(
        x=62.0,
        y=144.0,
        width=115.0,
        height=24.0
    )

    entry_quadro = Label(
        janela_enviados,
        textvariable=texto,
        bd=0.5,
        bg="#EFEFEF",
        fg="#000716",
        highlightthickness=0,
        wraplength = 500,
        relief = "sunken",
        font=("Bahnschrift SemiLight SemiConde", 20 * -1)
    )
    entry_quadro.place(
        x=45.0,
        y=194.0,
        width=518.0,
        height=206.0
    )

    canvas2.create_text(
        45.0,
        20.0,
        anchor="nw",
        text="Totais Enviados",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 14 * -1)
    )

    canvas2.create_text(
        420.0,
        15.0,
        anchor="nw",
        text="Total Geral:",
        fill="#000000",
        font=("Bahnschrift SemiLight SemiConde", 18 * -1)
    )

    janela_enviados.resizable(False, False)
 

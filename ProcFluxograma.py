# -*- coding: utf-8 -*-
import pandas as pd
import graphviz
import os

def gerar_fluxograma(file_path):
    df = pd.read_excel(file_path)

    dot = graphviz.Digraph(format="pdf")
    dot.attr(rankdir="TB", fontname="Roboto")

    # Corrigir nomes de colunas
    col_nome_processo = "NOME PROCESSO"
    col_inicio = "ATIVIDADE INÍCIO"
    col_origem = "ATIVIDADE ORIGEM"
    col_procedimento = "PROCEDIMENTO"
    col_destino = "ATIVIDADE DESTINO"

    for _, row in df.iterrows():
        origem = row[col_origem]
        destino = row[col_destino]
        procedimento = str(row[col_procedimento]) if not pd.isna(row[col_procedimento]) else ""

        dot.node(origem, origem, shape="box", style="rounded,filled", fillcolor="#E3F2FD", fontname="Roboto")
        if pd.notna(destino):
            dot.node(destino, destino, shape="box", style="rounded,filled", fillcolor="#FFF3E0", fontname="Roboto")
            dot.edge(origem, destino, label=procedimento, fontname="Roboto")

    # Salvar em múltiplos formatos
    base_output = os.path.splitext(file_path)[0]
    output_files = {}

    for ext in ["pdf", "png", "svg"]:
        output_path = f"{base_output}.{ext}"
        dot.render(filename=base_output, format=ext, cleanup=True)
        output_files[ext] = output_path

    return output_files

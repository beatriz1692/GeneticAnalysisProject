# src/report_generator.py
from reportlab.platypus import SimpleDocTemplate
from sequence_utils import obter_trecho_mutacao

def gerar_relatorio_pdf_profissional(nome_doenca, gene, variantes, sequencia, filename="relatorio.pdf"):
    # gera PDF com tabela de variantes e trechos de sequência
    pass

def gerar_relatorio_csv(nome_doenca, gene, variantes, sequencia, filename="relatorio.csv"):
    # gera CSV com todas as mutações e interpretações
    pass

# src/main.py
from clinvar_api import buscar_genes_por_doenca, buscar_variantes_clinvar
from ensembl_api import buscar_id_gene_ensembl, buscar_sequencia_gene_ensembl
from vep_analysis import consultar_impacto_vep, interpretar_impacto
from sequence_utils import obter_trecho_mutacao
from report_generator import gerar_relatorio_pdf_profissional

nome_doenca = input("Digite o nome da doença: ")

genes = buscar_genes_por_doenca(nome_doenca)
if not genes:
    gene = input("Nenhum gene encontrado automaticamente. Digite manualmente: ")
else:
    print("Genes encontrados:")
    for i, g in enumerate(genes):
        print(f"{i+1} - {g}")
    escolha = input("Escolha um gene pelo número ou digite outro manualmente (Enter para primeiro): ")
    if escolha.isdigit() and 1 <= int(escolha) <= len(genes):
        gene = genes[int(escolha)-1]
    elif escolha.strip() != "":
        gene = escolha.strip()
    else:
        gene = genes[0]

print(f"Gene selecionado: {gene}")
variantes = buscar_variantes_clinvar(gene)
gene_id = buscar_id_gene_ensembl(gene)
sequencia = buscar_sequencia_gene_ensembl(gene_id)

gerar_relatorio_pdf_profissional(nome_doenca, gene, variantes, sequencia)

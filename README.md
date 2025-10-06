Descrição do Projeto

O GeneticAnalysisProject é uma ferramenta em Python para análise clínica de variantes genéticas.
O programa permite ao usuário:
-Buscar genes associados a uma doença usando o ClinVar.
-Listar variantes conhecidas desses genes.
-Consultar o impacto funcional das mutações via VEP (Ensembl).
-Destacar mutações na sequência do gene, mostrando contexto ao redor.
-Gerar relatórios CSV e PDF com todas as informações organizadas, incluindo interpretação funcional/fisiológica das variantes.
-O projeto é útil para bioinformática clínica, pesquisa em genética e educação em interpretação de variantes.

Estrutura do Projeto
GeneticAnalysisProject/
│
├─ data/                       # Dados estáticos ou downloads
│   ├─ clinvar_raw/             # JSONs/CSVs do ClinVar (opcional)
│   └─ genes_sequences/         # Sequências de genes salvas (opcional)
│
├─ reports/                     # Relatórios gerados
│   ├─ csv/                     # Relatórios CSV
│   └─ pdf/                     # Relatórios PDF
│
├─ src/                         # Código-fonte
│   ├─ __init__.py
│   ├─ main.py                  # Programa principal
│   ├─ clinvar_api.py           # Funções para ClinVar
│   ├─ ensembl_api.py           # Funções para Ensembl
│   ├─ vep_analysis.py          # Consulta e interpretação VEP
│   ├─ sequence_utils.py        # Funções de manipulação de sequência
│   ├─ report_generator.py      # Geração de CSV/PDF
│   └─ config.py                # Configurações gerais
│
├─ requirements.txt             # Bibliotecas necessárias
└─ README.md / README.txt       # Este arquivo

Pré-requisitos:
-Python 3.8 ou superior
-Bibliotecas Python: requests; reportlab

Instale as dependências com:
pip install -r requirements.txt

Funcionalidades:
-Consulta automática de genes e variantes no ClinVar.
-Busca de ID e sequência do gene no Ensembl.
-Interpretação de impacto funcional das variantes via VEP.
-Destaque de mutações no DNA com contexto (±50 nucleotídeos).
-Relatórios organizados em CSV e PDF com todas as informações.
-Possibilidade de adicionar genes manualmente.

Referências:
NCBI ClinVar; Ensembl REST API; VEP – Variant Effect Predictor; ReportLab

Observações

O projeto depende de conexão com a internet para consultas ao ClinVar e Ensembl.

Nem todas as variantes podem ter impacto funcional conhecido.

O relatório PDF destaca apenas os trechos de sequência próximos às mutações para melhor visualização.

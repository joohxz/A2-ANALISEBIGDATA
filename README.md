# Análise de Desmatamento por Município e Bioma  
## A2 - Análise de Negócios com uso de Big Data

Este projeto realiza uma análise exploratória sobre dados de desmatamento, identificando os biomas mais afetados, o município mais crítico e gerando visualizações que auxiliam a tomada de decisão da fiscalização ambiental.

Autores:
- João Moraes Pereira Teixeira
- Matheus Diniz Walter Peixoto
- Daniel Dantas Duarte
- Weyglison Dirlan de Souza Pires
- Reymerson silva pimenta

---

## Dataset

**Arquivo:** `ambiental_desmatamento.csv`

**Colunas:**
- `municipio` — Nome do município
- `area_desmatada_ha` — Área desmatada em hectares
- `bioma` — Bioma ao qual o município pertence

**Exemplo do dataset:**

| municipio | area_desmatada_ha | bioma           |
|----------|--------------------|------------------|
| X        | 200                | Cerrado          |
| Y        | 150                | Cerrado          |
| Z        | 500                | Mata Atlântica   |
| W        | 80                 | Caatinga         |

---

## Objetivo do Projeto

- Identificar **quais biomas são mais afetados** pelo desmatamento.  
- Determinar **o município mais crítico** em termos de área desmatada.  
- Criar **visualizações** (heatmap e gráfico de barras).  
- Gerar um **relatório consolidado** para priorização ambiental.  
- Utilizar Python como ferramenta de análise de Big Data.

---

## Minimundo

A fiscalização ambiental deseja priorizar territórios que apresentam maior impacto ambiental.  
Para isso, foi fornecido um dataset contendo dados de municípios, biomas e áreas desmatadas.  
A análise deve gerar insights que apoiem ações estratégicas de monitoramento.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas** → Manipulação e agrupamento de dados  
- **Seaborn** → Geração de heatmap e gráficos  
- **Matplotlib** → Visualizações  
- **Jupyter / Script .py** → Execução do código

 por bioma:
| Bioma           | Área total (ha) |
|-----------------|------------------|
| Mata Atlântica  | 500              |
| Cerrado         | 350              |
| Caatinga        | 80               |

------
# ============================================================
# SISTEMA DE ANÁLISE DE DESMATAMENTO — MINIMUNDO 10
# ============================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CARREGAR O DATASET
df = pd.read_csv("ambiental_desmatamento.csv", encoding="utf-8")

print("Dados Carregados")
print(df)

# SOMATÓRIO DE ÁREA POR BIOMA
area_por_bioma = df.groupby("bioma")["area_desmatada_ha"].sum().reset_index()

print("\nÁrea Total Desmatada por Bioma")
print(area_por_bioma)

municipio_critico = df.loc[df["area_desmatada_ha"].idxmax()]

print("\n Município mais crítico")
print(f"Município: {municipio_critico['municipio']}")
print(f"Área Desmatada: {municipio_critico['area_desmatada_ha']} ha")
print(f"Bioma: {municipio_critico['bioma']}")

pivot = df.pivot_table(
    values="area_desmatada_ha",
    index="bioma",
    columns="municipio",
    aggfunc="sum"
)

# HEATMAP DE DESMATAMENTO POR BIOMA E MUNICÍPIO
plt.figure(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", linewidths=.5)
plt.title("Heatmap de Desmatamento por Bioma e Município")
plt.show()

# GRÁFICO DE BARRAS DESMATAMENTO POR BIOMA
plt.figure(figsize=(8, 5))
sns.barplot(data=area_por_bioma, x="bioma", y="area_desmatada_ha")
plt.title("Área Total Desmatada por Bioma")
plt.ylabel("Área (ha)")
plt.xlabel("Bioma")
plt.show()

# RELATÓRIO FINAL

print("\nRELATÓRIO FINAL DE PRIORIZAÇÃO")

print("\nBIOMAS PRIORITÁRIOS (MAIOR DESMATAMENTO):")
for i, row in area_por_bioma.sort_values(by="area_desmatada_ha", ascending=False).iterrows():
    print(f" - {row['bioma']}: {row['area_desmatada_ha']} ha")

print("\nMUNICÍPIO MAIS CRÍTICO:")
print(f" - {municipio_critico['municipio']} ({municipio_critico['area_desmatada_ha']} ha, Bioma: {municipio_critico['bioma']})")

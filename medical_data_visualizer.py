import pandas as pd # pyright: ignore[reportMissingModuleSource]
import seaborn as sns # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]

# 1
df = pd.read_csv("medical_examination.csv")

# 2
overweightData = []
for i in range(len(df["weight"])):
    if df["weight"][i]/(df["height"][i]**2) > 25:
        overweightData.append(1)
    else:
        overweightData.append(0)
df['overweight'] = overweightData

# 3
newChol = []
newGluc = []

for i in range(len(df["cholesterol"])):
    if df["cholesterol"][i] >= 1:
        newChol.append(1)
    else:
        newChol.append(0)
df["cholesterol"] = newChol

for i in range(len(df["gluc"])):
    if df["gluc"][i] >= 1:
        newGluc.append(1)
    else:
        newGluc.append(0)
df["gluc"] = newGluc

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    df_cat['total'] = df_cat['total']
    
    # 7
    g = sns.catplot(x="variable", y="total", legend="auto", legend_out=True, hue="value", kind="bar", data=df_cat, col="cardio", errorbar=None)

    # 8
    fig = g.figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

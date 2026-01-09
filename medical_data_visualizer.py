import pandas as pd # pyright: ignore[reportMissingModuleSource]
import seaborn as sns # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]

# 1
df = pd.read_csv("medical_examination.csv")

# 2: compute BMI correctly (height is in cm -> convert to meters)
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
newChol = []
newGluc = []

# normalize cholesterol and gluc: 1 -> 0 (normal), >1 -> 1 (elevated)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

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
    df_heat = df.copy()

    # build a boolean mask using bitwise operators (Series require & not `and`)
    # *HELP WITH COPILOT WAS USED - I DID NOT UNDERSTAND HOW THIS FUNCTION WORKS*
    mask = (
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
    )

    df_heat = df_heat[mask]

    # 12
    corr = df_heat.corr(numeric_only=True)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(15, 10))

    # 15: plot onto the Axes and keep the Figure in `fig`
    sns.heatmap(data=corr, annot=True, fmt='.1f', cbar=True, mask=mask, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig

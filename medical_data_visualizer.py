import pandas as pd # pyright: ignore[reportMissingModuleSource]
import seaborn as sns # pyright: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]

# 1
df = pd.read_csv("medical_examination.csv")

# 2
overweightData = int(df["weight"]/(df["height"]**2) > 25)
df['overweight'] = overweightData

# 3
df["cholesterol"] = int(df["cholesterol"] > 1)
df["gluc"] = int(df["gluc"] > 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


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

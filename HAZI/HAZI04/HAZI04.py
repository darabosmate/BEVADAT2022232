#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


def csv_to_df(path:str)->pd.core.frame.DataFrame:
    ndf = pd.read_csv(path)
    return ndf

def capitalize_columns(df_data:pd.DataFrame) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_column_names = new_df.columns.to_series().apply(lambda x: x.upper() if 'e' not in x.lower() else x)
    new_df.rename(columns=new_column_names, inplace=True)
    return new_df

def math_passed_count(df_data: pd.core.frame.DataFrame)-> int:
    ndf = df_data.copy()
    return sum(ndf["math score"]>50)

def did_pre_course(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    return ndf.loc[ndf["test preparation course"] == "completed"]

def average_scores(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    return ndf.groupby(["parental level of education"]).mean()

def add_age(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    np.random.seed(42)
    ndf["age"] = np.random.randint(18, 66)
    return ndf

def female_top_score(df: pd.DataFrame)->tuple:
    ndf = df.copy()
    return tuple(ndf.loc[ndf["gender"] == "female"].max())[5:]

def add_grade(df_data:pd.DataFrame) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_df['percent'] = (new_df['math score'] + new_df['reading score'] + new_df['writing score']) / 300
    new_df['grade'] = pd.cut(new_df['percent'], bins=[0, 0.6, 0.7, 0.8, 0.9, 1], labels=['F', 'D', 'C', 'B', 'A'])
    new_df.drop('percent', axis=1, inplace=True)
    return new_df

def math_bar_plot(df:pd.DataFrame)-> plt.Figure:
    ndf = df.copy()
    avg_per_gender = ndf.groupby("gender")["math score"].mean()
    fig, ax = plt.subplots()
    ax.bar(avg_per_gender.index, avg_per_gender.values)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    ax.set_title('Average Math Score by Gender')
    
    return fig

def writing_hist(df: pd.DataFrame)->plt.Figure:
    ndf = df.copy()
    x = ndf['writing score']

    fig, ax = plt.subplots()

    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')

    plt.hist(x)

    return fig

''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''





df = csv_to_df("/home/mate/Documents/repos/BEVADAT2022232/HAZI/HAZI04/StudentsPerformance.csv")
print(type(writing_hist(df)))

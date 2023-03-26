#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

#1
def csv_to_df(path:str)->pd.core.frame.DataFrame:
    ndf = pd.read_csv(path)
    return ndf
#2
def capitalize_columns(df_data:pd.DataFrame) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_column_names = new_df.columns.to_series().apply(lambda x: x.upper() if 'e' not in x.lower() else x)
    new_df.rename(columns=new_column_names, inplace=True)
    return new_df
#3
def math_passed_count(df_data: pd.core.frame.DataFrame)-> int:
    ndf = df_data.copy()
    c = len(ndf[ndf["math score"]>=50])
    return c
#4
def did_pre_course(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    return ndf.loc[ndf["test preparation course"] == "completed"]
#5
def average_scores(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    return ndf.groupby(["parental level of education"]).mean()
#6
def add_age(df: pd.DataFrame)->pd.core.frame.DataFrame:
    ndf = df.copy()
    random.seed(42)
    age = [random.randint(18, 67) for x in range(ndf.shape[0])]
    ndf['age'] = age

    return ndf
#7
def female_top_score(df: pd.DataFrame)->tuple:
    ndf = df.copy()
    return tuple(ndf.loc[ndf["gender"] == "female"].max())[5:]
#8
def add_grade(df_data:pd.DataFrame) -> pd.core.frame.DataFrame:
    new_df = df_data.copy()
    new_df['percent'] = (new_df['math score'] + new_df['reading score'] + new_df['writing score']) / 300
    new_df['grade'] = pd.cut(new_df['percent'], bins=[0, 0.6, 0.7, 0.8, 0.9, 1], labels=['F', 'D', 'C', 'B', 'A'])
    new_df.drop('percent', axis=1, inplace=True)
    return new_df
#9
def math_bar_plot(df:pd.DataFrame)-> plt.Figure:
    ndf = df.copy()
    avg_per_gender = ndf.groupby("gender")["math score"].mean()
    fig, ax = plt.subplots()
    ax.bar(avg_per_gender.index, avg_per_gender.values)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    ax.set_title('Average Math Score by Gender')
    
    return fig
#10
def writing_hist(df: pd.DataFrame)->plt.Figure:
    ndf = df.copy()
    x = ndf['writing score']

    fig, ax = plt.subplots()

    ax.hist(x)

    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')

    return fig
#11
def ethnicity_pie_chart(df: pd.DataFrame)->plt.Figure:
    ndf = df.copy()
    x = ndf['race/ethnicity'].value_counts()
    fig, ax = plt.subplots()
    ax.set_title("Proportion of Students by Race/Ethnicity")
    ax.pie(x.values, labels=x.index, autopct='%1.1f%%')
    return fig

#df = csv_to_df("/home/mate/Documents/repos/BEVADAT2022232/HAZI/HAZI04/StudentsPerformance.csv")
#ethnicity_pie_chart(df)
# %%

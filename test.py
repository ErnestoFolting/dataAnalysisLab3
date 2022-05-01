from dataclasses import replace
import pandas as pd 
import matplotlib.pyplot as plt

def read_dataset():
    data = pd.read_csv('Data1.csv',sep=';')
    return data 

def print_first_five_rows(dataset):
    print(dataset.head(5))

def print_last_six_rows(dataset):
    print(dataset.tail(6))

def delete_iso(dataset):
    return dataset.drop('ISO',axis = 1)

def convert_column_to_float(dataset,column_label):
    dataset[column_label] = dataset[column_label].str.replace(',', '.').astype(float)

def add_total_gdp(dataset):
    dataset['Total GDP'] = dataset['Population'] * dataset["GDP per capita"]

def replace_blank_with_zeros(dataset):
    return dataset.replace(' ',0)

def gdp_per_capita_boxplot(dataset):
    plt.figure()
    plt.title('Діаграма розмаху для GDP per capita')
    plt.boxplot(dataset['GDP per capita'])

def plot_tech_exports_from_gdp_dependency(dataset):
    plt.figure()
    plt.title('Залежність High-technology exports від GDP per capita')
    plt.xlabel('GDP per capita')
    plt.ylabel('High-technology exports')
    plt.plot(
        dataset['GDP per capita'],
        dataset['High-technology exports'],
        '*'
    )

#calls
dataset = read_dataset()
dataset = delete_iso(dataset)
convert_column_to_float(dataset,'Population')
add_total_gdp(dataset)
dataset = replace_blank_with_zeros(dataset)
gdp_per_capita_boxplot(dataset)
plot_tech_exports_from_gdp_dependency(dataset)
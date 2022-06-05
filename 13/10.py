import pandas as pd
from numpy import NAN

df = pd.read_csv('Pokemon.csv').drop_duplicates('#').set_index('Name')
type_chart = pd.read_csv('type_chart.csv')  # скопировано с https://pokemondb.net/type. доступно на https://docs.google.com/spreadsheets/d/1HZkLd8-TAMfZLAFSlwTjZZV9Cmv-RNSCq1Ow2sR9Jzo/edit?usp=sharing
type_chart = type_chart.set_index('Type').replace(NAN, 1)
type_chart.at['FIGHTING', 'NORMAL']
type_chart


def fight(first, second):
    first_types = pd.Series((df.at[first, 'Type 1'], df.at[first, 'Type 2'])).dropna().str.upper()
    second_types = pd.Series((df.at[second, 'Type 1'], df.at[second, 'Type 2'])).dropna().str.upper()

    first_attack = second_attack = 1
    for ft in first_types:
        for st in second_types:
            first_attack *= type_chart.at[ft, st]
            second_attack *= type_chart.at[st, ft]

    if first_attack > second_attack:
        return first
    if second_attack > first_attack:
        return second
    return 'draw'


fight('Bulbasaur', 'Squirtle')

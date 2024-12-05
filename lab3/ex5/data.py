import pandas as pd

vgsales = pd.read_csv('vgsales.csv')
metacritic_games = pd.read_csv('metacritic_games.csv')

__all__ = ['vgsales', 'metacritic_games']

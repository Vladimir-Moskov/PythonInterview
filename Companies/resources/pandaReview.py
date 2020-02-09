"""
    Review of main Panda features

    https://pandas.pydata.org/
    Python Data Analytics: With Pandas, NumPy, and Matplotlib
"""
import pandas
import matplotlib.pyplot as pyplot
import numpy

# %matplotlib inline

# read excel sheet to data frame
titanic_df = pandas.read_excel('titanic.xlsx', 'complete', index_col=None, na_values=['NA'])
print(titanic_df.head())


print(titanic_df.describe())

titanic_df = titanic_df.drop(['ticket', 'boat', 'cabin', 'body'], axis=1)
print(titanic_df.head())

print(titanic_df.isnull().sum())
pandas.value_counts(titanic_df['survived']).plot.bar()
# pyplot.show()

print(titanic_df.mean())
print(titanic_df['survived'].mean())


print(titanic_df.groupby(['sex']).mean())
print(titanic_df.groupby(['sex', 'pclass']).mean())

print(titanic_df[titanic_df['age'] < 18].groupby(['sex', 'pclass']).mean())







import matplotlib.pyplot as plt
import pandas as pd 
from getdata import df_stats
import numpy as np

stats_summary = df_stats.describe()
print(stats_summary)


plt.hist(df_stats['firstNumberMean'], bins=20, alpha=0.5, label='First Number')
plt.hist(df_stats['secondNumberMean'], bins=20, alpha=0.5, label='Second Number')
plt.hist(df_stats['thirdNumberMean'], bins=20, alpha=0.5, label='Third Number')
plt.hist(df_stats['fourthNumberMean'], bins=20, alpha=0.5, label='Fourth Number')
plt.hist(df_stats['fifthNumberMean'], bins=20, alpha=0.5, label='Fifth Number')
plt.xlabel('Mean')
plt.ylabel('Frequency')
plt.title('Distribution of Means')
plt.legend()
plt.show()


# Create a chart of numbers that have not been drawn recently and sort by length since drawn
df_stats['firstNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['firstNumberDaysSinceDrawn'])
df_stats['secondNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['secondNumberDaysSinceDrawn'])
df_stats['thirdNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['thirdNumberDaysSinceDrawn'])
df_stats['fourthNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['fourthNumberDaysSinceDrawn'])
df_stats['fifthNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['fifthNumberDaysSinceDrawn'])
df_stats['powerballNumberDaysSinceDrawn'] = pd.to_numeric(df_stats['powerballNumberDaysSinceDrawn'])

##top 10 of all numbers that have not been drawn recently
df_stats.sort_values(by=['firstNumberDaysSinceDrawn', 'secondNumberDaysSinceDrawn', 'thirdNumberDaysSinceDrawn',
                         'fourthNumberDaysSinceDrawn', 'fifthNumberDaysSinceDrawn', 'powerballNumberDaysSinceDrawn'],
                     ascending=False, inplace=True)
df_stats_top10 = df_stats.head(10)

#A chart
plt.bar(df_stats['firstNumberDaysSinceDrawn'], df_stats['firstNumber'], color='b', alpha=0.7)
plt.bar(df_stats['secondNumberDaysSinceDrawn'], df_stats['secondNumber'], color='r', alpha=0.7)
plt.bar(df_stats['thirdNumberDaysSinceDrawn'], df_stats['thirdNumber'], color='g', alpha=0.7)
plt.bar(df_stats['fourthNumberDaysSinceDrawn'], df_stats['fourthNumber'], color='y', alpha=0.7)
plt.bar(df_stats['fifthNumberDaysSinceDrawn'], df_stats['fifthNumber'], color='c', alpha=0.7)
plt.bar(df_stats['powerballNumberDaysSinceDrawn'], df_stats['powerballNumber'], color='m', alpha=0.7)
plt.bar
plt.title('Numbers That Have Not Been Drawn Recently')
plt.xlabel('Days Since Drawn')
plt.ylabel('Number')
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
#import pytorch as torch


from getdata import df_drawings

# Descriptive statistics for the "Jackpot" column
jackpot_stats = df_drawings['Jackpot'].describe()

# Frequency of each number in "Winning Numbers"
number_frequency = df_drawings['Winning Numbers'].explode().value_counts()
number_frequency.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers in Winning Numbers')
plt.show()


#Distribution of the jackpots freqeuncy 
plt.hist(df_drawings['Jackpot'], bins=20)
plt.xlabel('Jackpot')
plt.ylabel('Frequency')
plt.title('Distribution of Jackpots')
plt.show()

# Scatter plot of the jackpot size vs. the number of winners
df_drawings.plot.scatter(x="Jackpot", y="Winners")
plt.xlabel('Jackpot')
plt.ylabel('Winners')
plt.title('Jackpot vs. Winners')
plt.show()

# Histogram of the jackpot size
df_drawings.hist(column="Jackpot")
plt.xlabel('Jackpot')
plt.ylabel('Frequency')
plt.title('Distribution of Jackpots')
plt.show()


# Scatter plot of the jackpot size vs. the number of winners
df_drawings.plot.scatter(x="Jackpot", y="Winners")
plt.xlabel('Jackpot')
plt.ylabel('Winners')
plt.title('Jackpot vs. Winners')
plt.show()








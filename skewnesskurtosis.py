import pandas as pd
import matplotlib.pyplot as plt
from getdata import df_stats

# Convert whiteball occurrences and powerball occurrences to a DataFrame
df_whiteball_occurrences = pd.DataFrame(list(df_stats['whiteballoccurrences'].items()), columns=['Number', 'Occurrences'])
df_powerball_occurrences = pd.DataFrame(list(df_stats['powerballoccurrences'].items()), columns=['Number', 'Occurrences'])

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(20, 10))

# Bar plot for whiteball occurrences
ax[0].bar(df_whiteball_occurrences['Number'], df_whiteball_occurrences['Occurrences'], color='b', alpha=0.7)
ax[0].set_title('Occurrences of Whiteball Numbers')
ax[0].set_xlabel('Number')
ax[0].set_ylabel('Occurrences')

# Bar plot for powerball occurrences
ax[1].bar(df_powerball_occurrences['Number'], df_powerball_occurrences['Occurrences'], color='r', alpha=0.7)
ax[1].set_title('Occurrences of Powerball Numbers')
ax[1].set_xlabel('Number')
ax[1].set_ylabel('Occurrences')

# Display the plots
plt.tight_layout()
plt.show()



# Create new dataframes that include skewness and kurtosis for each number
df_whiteball_stats = pd.DataFrame({
    'Number': df_whiteball_occurrences['Number'],
    'Occurrences': df_whiteball_occurrences['Occurrences'],
    'Skewness': [df_stats[f'{number}NumberSampleSkewness'].values[0] for number in df_whiteball_occurrences['Number']],
    'Kurtosis': [df_stats[f'{number}NumberSampleKurtosis'].values[0] for number in df_whiteball_occurrences['Number']]
})

df_powerball_stats = pd.DataFrame({
    'Number': df_powerball_occurrences['Number'],
    'Occurrences': df_powerball_occurrences['Occurrences'],
    'Skewness': [df_stats[f'{number}NumberSampleSkewness'].values[0] for number in df_powerball_occurrences['Number']],
    'Kurtosis': [df_stats[f'{number}NumberSampleKurtosis'].values[0] for number in df_powerball_occurrences['Number']]
})
##############################################################################################################
# Scatter plots
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# Whiteball occurrences vs skewness
ax[0, 0].scatter(df_whiteball_stats['Occurrences'], df_whiteball_stats['Skewness'])
ax[0, 0].set_title('Whiteball Occurrences vs Skewness')
ax[0, 0].set_xlabel('Occurrences')
ax[0, 0].set_ylabel('Skewness')

# Whiteball occurrences vs kurtosis
ax[0, 1].scatter(df_whiteball_stats['Occurrences'], df_whiteball_stats['Kurtosis'])
ax[0, 1].set_title('Whiteball Occurrences vs Kurtosis')
ax[0, 1].set_xlabel('Occurrences')
ax[0, 1].set_ylabel('Kurtosis')

# Powerball occurrences vs skewness
ax[1, 0].scatter(df_powerball_stats['Occurrences'], df_powerball_stats['Skewness'])
ax[1, 0].set_title('Powerball Occurrences vs Skewness')
ax[1, 0].set_xlabel('Occurrences')
ax[1, 0].set_ylabel('Skewness')

# Powerball occurrences vs kurtosis
ax[1, 1].scatter(df_powerball_stats['Occurrences'], df_powerball_stats['Kurtosis'])
ax[1, 1].set_title('Powerball Occurrences vs Kurtosis')
ax[1, 1].set_xlabel('Occurrences')
ax[1, 1].set_ylabel('Kurtosis')

# Display the plots
plt.tight_layout()
plt.show()

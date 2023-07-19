import numpy as np
import matplotlib.pyplot as plt

from getdata import df_stats

# Data for the plots
numbers = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
variances = [df_stats['firstNumberVariance'].values[0], df_stats['secondNumberVariance'].values[0],
             df_stats['thirdNumberVariance'].values[0], df_stats['fourthNumberVariance'].values[0],
             df_stats['fifthNumberVariance'].values[0]]
skewness = [df_stats['firstNumberSampleSkewness'].values[0], df_stats['secondNumberSampleSkewness'].values[0],
            df_stats['thirdNumberSampleSkewness'].values[0], df_stats['fourthNumberSampleSkewness'].values[0],
            df_stats['fifthNumberSampleSkewness'].values[0]]
kurtosis = [df_stats['firstNumberSampleKurtosis'].values[0], df_stats['secondNumberSampleKurtosis'].values[0],
            df_stats['thirdNumberSampleKurtosis'].values[0], df_stats['fourthNumberSampleKurtosis'].values[0],
            df_stats['fifthNumberSampleKurtosis'].values[0]]

# Create subplots
fig, ax = plt.subplots(3, 1, figsize=(10, 15))

# Bar plot for variances
ax[0].bar(numbers, variances, color='b', alpha=0.7)
ax[0].set_title('Variance of Each Number')
ax[0].set_ylabel('Variance')

# Bar plot for skewness
ax[1].bar(numbers, skewness, color='r', alpha=0.7)
ax[1].set_title('Skewness of Each Number')
ax[1].set_ylabel('Skewness')

# Bar plot for kurtosis
ax[2].bar(numbers, kurtosis, color='g', alpha=0.7)
ax[2].set_title('Kurtosis of Each Number')
ax[2].set_ylabel('Kurtosis')

# Display the plots
plt.tight_layout()
plt.show()

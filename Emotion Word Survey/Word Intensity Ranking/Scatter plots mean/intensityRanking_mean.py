# script to create scatter plot for mean intensity ranking in three emotion
# categories. refer to readme for more information about survey and ranking
# task.

# 18 November 2018, Pulkit Singh

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#----------------------------------------------------------------------------#

# Sadness Category 

sad_labels = ['displeased', 'unhappy', 'sad', 'dejected', 'miserable',
			  'heartbroken', 'depressed']
sad_means  = [1.38, 1.94, 2.56, 3.44, 4.22, 4.33, 4.38]
sad_x = list(range(1, len(sad_means) + 1))

# plotting means
sad_plt, sad_ax = plt.subplots(figsize=(9, 9))
sad_ax = sns.scatterplot(sad_x, sad_means, marker="")

# annotating data points
for i in range(len(sad_means)):
	sad_ax.annotate(sad_labels[i], (sad_x[i], sad_means[i]))

plt.xlabel("Words in 'sadness' category")
plt.ylabel("Average intensity ranking \n")
plt.title("Average intensity ranking of 'sadness' category words")
plt.xlim((0, 10))
plt.ylim((1, 5))
plt.xticks([], [])
plt.savefig("IR_mean_sadness.png")

#----------------------------------------------------------------------------#

# Anger Category
anger_labels = ['irked', 'annoyed', 'irritated', 'mad', 'incensed',
			  'angry', 'infuriated', 'enraged']
anger_means  = [1.83, 1.94, 2.44, 2.88, 3.22, 3.38, 4.55, 4.72]
anger_x = list(range(1, len(anger_means) + 1))

# plotting means
anger_plt, anger_ax = plt.subplots(figsize=(9, 9))
anger_ax = sns.scatterplot(anger_x, anger_means, marker="")

# annotating data points
for i in range(len(anger_means)):
	anger_ax.annotate(anger_labels[i], (anger_x[i], anger_means[i]))

plt.xlabel("Words in 'anger' category")
plt.ylabel("Average intensity ranking \n")
plt.title("Average intensity ranking of 'anger' category words")
plt.xlim((0, 10))
plt.ylim((1, 5))
plt.xticks([], [])
plt.savefig("IR_mean_anger.png")

#----------------------------------------------------------------------------#

# Fear Category

fear_labels = ['afraid', 'scared', 'intimidated', 'alarmed', 'distressed',
			   'frightened', 'horrified', 'terrified']
fear_means  = [2.27, 2.27, 2.33, 2.38, 2.66, 3.05, 4.38, 4.55]
fear_x = list(range(1, len(fear_means) + 1))

# plotting means
fear_plt, fear_ax = plt.subplots(figsize=(9, 9))
fear_ax = sns.scatterplot(fear_x, fear_means, marker="")

# annotating data points
for i in range(len(fear_means)):
	fear_ax.annotate(fear_labels[i], (fear_x[i], fear_means[i]))

plt.xlabel("Words in 'fear' category")
plt.ylabel("Average intensity ranking \n")
plt.title("Average intensity ranking of 'fear' category words")
plt.xlim((0, 10))
plt.ylim((1, 5))
plt.xticks([], [])
plt.savefig("IR_mean_fear.png")

#----------------------------------------------------------------------------#
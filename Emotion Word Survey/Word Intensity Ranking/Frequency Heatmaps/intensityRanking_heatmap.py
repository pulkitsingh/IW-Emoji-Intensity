# script to create frequency heatmaps for intensity ranking survey regardings
# words in three categories. Refer to readme for details about survey and
# ranking task.

# 18 November 2018, Pulkit Singh

#----------------------------------------------------------------------------#

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#----------------------------------------------------------------------------#

# Sadness Category

sad = pd.read_csv("IR_freq_sadness.csv")
sad_plt, sad_ax = plt.subplots(figsize=(6 , 6))
sad_ax = sns.heatmap(sad.transpose(), annot=True, fmt='d', linewidths=0.5,
					 square=True, xticklabels=[1,2,3,4,5])
plt.xlabel("\n Intensity Scale: 1 (mild) to 5 (intense)")
plt.title("Frequency of Intensity Rankings for 'Sadness' Category words \n")
plt.savefig("sadness_heatmap.png")

#----------------------------------------------------------------------------#

# Fear Category

fear = pd.read_csv("IR_freq_fear.csv")
fear_plt, fear_ax = plt.subplots(figsize=(6 , 6))
fear_ax = sns.heatmap(fear.transpose(), annot=True, fmt='d', linewidths=0.5,
					  square=True, xticklabels=[1,2,3,4,5])
plt.xlabel("\n Intensity Scale: 1 (mild) to 5 (intense)")
plt.title("Frequency of Intensity Rankings for 'Fear' Category words \n")
plt.savefig("fear_heatmap.png")

#----------------------------------------------------------------------------#

# Anger Category

anger = pd.read_csv("IR_freq_anger.csv")
anger_plt, anger_ax = plt.subplots(figsize=(6 , 6))
anger_ax = sns.heatmap(anger.transpose(), annot=True, fmt='d', linewidths=0.5,
					   square=True, xticklabels=[1,2,3,4,5])
plt.xlabel("\n Intensity Scale: 1 (mild) to 5 (intense)")
plt.title("Frequency of Intensity Rankings for 'Anger' Category words \n")
plt.savefig("anger_heatmap.png")

#----------------------------------------------------------------------------#


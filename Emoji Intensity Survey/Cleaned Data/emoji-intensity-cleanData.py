# script to clean data collected using Amazon MTurk. Format of task is to
# rate each emoji on a scale of 1 (most mild) to 5 (most intense)

# Independent Work: Intensity Encoding for Emojis
# December 3, 2018
# Pulkit Singh

#------------------------------------------------------------------------------#

import pandas as pd 

#------------------------------------------------------------------------------#

# selects relevant columns of options and answers, cleans up links and returns
# 2 x N dataframe of emoji names and intensity rankings
def cleanData(dataFile, emojiLinks, emojiNames):

	# selecting relevant columns
	col_names  = ['Input.emoji', 'Answer.rate']

	df = pd.read_csv(dataFile, usecols=col_names)

	# replacing links to emoji images with names of emojis
	df.replace(to_replace=emojiLinks, value=emojiNames, inplace=True)

	# making the ratings column into integers
	df['Answer.rate'] = pd.to_numeric(df['Answer.rate'])

	return df


#------------------------------------------------------------------------------#

angryLinks = ['https://s3.us-east-2.amazonaws.com/iw-emojis/angry.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/pouting.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/angry_steam.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/angry_horns.png']
angryNames = ['angry', 'pouting', 'steam', 'horns']

#------------------------------------------------------------------------------#

fearLinks = ['https://s3.us-east-2.amazonaws.com/iw-emojis/fear_astonished.png',
			 'https://s3.us-east-2.amazonaws.com/iw-emojis/fear_cat.png',
			 'https://s3.us-east-2.amazonaws.com/iw-emojis/fear_fearful.png',
			 'https://s3.us-east-2.amazonaws.com/iw-emojis/fear_scream.png',
			 'https://s3.us-east-2.amazonaws.com/iw-emojis/fear_sweat.png']
fearNames  = ['astonished', 'cat', 'fearful', 'scream', 'sweat']

#------------------------------------------------------------------------------#

sadLinks = ['https://s3.us-east-2.amazonaws.com/iw-emojis/sad_crying.png',
			'https://s3.us-east-2.amazonaws.com/iw-emojis/sad_disappointed.png',
			'https://s3.us-east-2.amazonaws.com/iw-emojis/sad_pensive.png',
			'https://s3.us-east-2.amazonaws.com/iw-emojis/sad_tear.png',
			'https://s3.us-east-2.amazonaws.com/iw-emojis/sad_tired.png',
			'https://s3.us-east-2.amazonaws.com/iw-emojis/sad_weary.png']
sadNames   = ['crying', 'disappointed', 'pensive', 'tear', 'tired', 'weary']

#------------------------------------------------------------------------------#

# cleaning and saving data in csv files
anger_clean = cleanData("emoji-intensity-anger-results.csv", angryLinks, 
						angryNames)
fear_clean  = cleanData("emoji-intensity-fear-results.csv", fearLinks, 
						fearNames)
sad_clean   = cleanData("emoji-intensity-sadness-results.csv", sadLinks, 
						sadNames)


anger_clean.to_csv("EI-anger-clean.csv")
fear_clean.to_csv("EI-fear-clean.csv")
sad_clean.to_csv("EI-sad-clean.csv")

#------------------------------------------------------------------------------#

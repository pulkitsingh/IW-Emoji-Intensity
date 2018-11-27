# script to clean data collected using Amazon MTurk. Format of task is to
# select between two emojis based on intensity, e.g. "Which emoji is more
# angry?"

# Independent Work: Intensity Encoding for Emojis
# November 27, 2018
# Pulkit Singh

#------------------------------------------------------------------------------#

import pandas as pd 

#------------------------------------------------------------------------------#

# helper function that populates 'answer' column using the emojis and human
# response in each row of the data
def choice(row):
	if str(row['Answer.choice']) == 'optionA':
		return row['Input.emoji_1']
	else:
		return row['Input.emoji_2']

#------------------------------------------------------------------------------#

# selects relevant columns of options and answers, cleans up links and returns
# 5 x N DataFrame
def cleanData(dataFile, emojiLinks, emojiNames):

	# selecting relevant columns
	col_names  = ['Input.type', 'Input.emotion', 'Input.emoji_1', 
				  'Input.emoji_2','Answer.choice']

	df = pd.read_csv(dataFile, usecols=col_names)

	# replacing links to emoji images with names of emojis
	df.replace(to_replace=emojiLinks, value=emojiNames, inplace=True)

	# populating answers column
	df['answers'] = df.apply(choice, axis=1)

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

# cleaning all raw data files
anger_more = cleanData("anger-more-results.csv", angryLinks, angryNames)
anger_less = cleanData("anger-less-results.csv", angryLinks, angryNames)
fear_more  = cleanData("fear-more-results.csv", fearLinks, fearNames)
fear_less  = cleanData("fear-less-results.csv", fearLinks, fearNames)
sad_more   = cleanData("sad-more-results.csv", sadLinks, sadNames)
sad_less   = cleanData("sad-less-results.csv", sadLinks, sadNames)

# saving cleaned data in csv files
anger_more.to_csv("anger-more-clean.csv")
anger_less.to_csv("anger-less-clean.csv")
fear_more.to_csv("fear-more-clean.csv")
fear_less.to_csv("fear-less-clean.csv")
sad_more.to_csv("sad-more-clean.csv")
sad_less.to_csv("sad-less-clean.csv")

#------------------------------------------------------------------------------#

# script to clean data collected using Amazon MTurk. Format of task is to
# select the emoji closest to a word. For example, which emoji is most 
# similar to the word "terrified"? [choice between 5 emojis]

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
	elif str(row['Answer.choice']) == 'optionB':
		return row['Input.emoji_2']
	elif str(row['Answer.choice']) == 'optionC':
		return row['Input.emoji_3']
	elif str(row['Answer.choice']) == 'optionD':
		return row['Input.emoji_4']
	elif str(row['Answer.choice']) == 'optionE':
		return row['Input.emoji_5']
	else:
		return row['Input.emoji_6']

#------------------------------------------------------------------------------#

# selects relevant columns of options and answers, cleans up links and returns
# 5 x N DataFrame
def cleanData(dataFile, emojiLinks, emojiNames):

	# selecting relevant columns
	col_names  = ['Input.word','Input.emoji_1','Input.emoji_2','Input.emoji_3', 
				  'Input.emoji_4','Input.emoji_5','Input.emoji_6',
				  'Answer.choice']

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
#ewa_anger = cleanData("ewa-anger.csv", angryLinks, angryNames)
#ewa_fear  = cleanData("ewa-fear.csv", fearLinks, fearNames)
ewa_sad   = cleanData("ewa-sadness.csv", sadLinks, sadNames)


# saving cleaned data files
#ewa_anger.to_csv("ewa-anger-clean.csv")
#ewa_fear.to_csv("ewa-fear-clean.csv")
ewa_sad.to_csv("ewa-sad-clean.csv")

#------------------------------------------------------------------------------#

# grouping data by word and response to produce frequency table
#anger_count = ewa_anger.groupby(['Input.word', 'answers'])['answers'].count()
#fear_count  = ewa_fear.groupby(['Input.word', 'answers'])['answers'].count()
sad_count   = ewa_sad.groupby(['Input.word', 'answers'])['answers'].count()

# saving frequency tables in data files
#anger_count.to_csv("ewa-anger-count.csv")
#fear_count.to_csv("ewa-fear-count.csv")
sad_count.to_csv("ewa-sad-count.csv")

#------------------------------------------------------------------------------#
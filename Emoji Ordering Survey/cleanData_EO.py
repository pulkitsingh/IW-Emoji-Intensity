import pandas as pd 



#----------------------------------------------------------------------------#

def cleanData(emojiLinks, emojiNames):
	col_names  = ['Input.type', 'Input.emotion', 'Input.emoji_1', 
				  'Input.emoji_2','Answer.choice']

	df = pd.read_csv("anger-more-results.csv", usecols=col_names)

	df.replace(emojiLinks, emojiNames, inplace=True)

	df['answers'] = df.apply(choice, axis=1)
	print df


def choice(row):
	if str(row['Answer.choice']) == 'optionA':
		return row['Input.emoji_1']
	else:
		return row['Input.emoji_2']




angryLinks = ['https://s3.us-east-2.amazonaws.com/iw-emojis/angry.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/pouting.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/angry_steam.png',
			  'https://s3.us-east-2.amazonaws.com/iw-emojis/angry_horns.png']
angryNames = ['angry', 'pouting', 'steam', 'horns']


cleanData(angryLinks, angryNames)

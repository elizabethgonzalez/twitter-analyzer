# credibility algorithhm

# how these parameters work
	# user will be either be rewarded or marked down based on twitter usage
	
# FUNCTIONS WE NEED

# determine user flags and return score
	# determine if user has been flagged for abuse
	# determine if they send hate speech, racist / sexist comments
	# this will bring down user score

# determine fact vs opinion writing
	# can take avg of how much user uses opinion vs fact based writingn
	# comparing the averages, determine score 
	# its gonna be hard to determine fact vs opinon based writing, 
	# well need to research more apis to help us here
	# how do we take into account like normally 
	# can find api that distinguishes how many logical fallacies a person has
	# implement a fact checker? 
	
import requests
from textblob import TextBlob
import hatebaase

# Take in user's tweet
msg = input('tweet\n')

#Determine user subjectivity vs logc, keywords and polarity
blob = TextBlob(msg)
opinions = blob.subjectivity
extreme = blob.polarity
phrases = blob.noun_phrases # keyword phrases
keywords = []
for nouns in phrases:
	keywords.append(nouns) # converting keywords from WordList to list

# Unable to get this data from Twitter APIs so I made my own below
# flags = {
# 	'not_interest': 0,
# 	'spam': {'fake': '', 'phish': '', 'hashtags': '', 'reply': '', 'else': ''},
# 	'abusive': {'disrespectful': '', 'private': '', 
# 		'harassment': '', 'direct_hate': '', 'threatening': '', 'self_harm': ''},
# 	'misleading': {'false_info': '', 'suppress': '', 'misrepresents': ''},
# 	'self_harm': '',
# }

# Determining abuse and hate speech percentage
hatespeech = hatebaase.hatebase()
bank = []
for i in range(0, len(hatespeech)):
	if hatespeech[i] in msg:
		bank.append(hatespeech[i])

# Calculating percentage
length = len(bank)
if length > 10:
	abuse = 1
elif length > 1:
	abuse = length/10
else:
	abuse = 0

# ADD UP FINAL SCORE
baseline = 50
score = (baseline - opinions*20 - abs(extreme)*10 - abuse*20)/baseline*100

# OUTPUT
user_metrics = {
	'subjectivity': opinions,
	'polarity': extreme,
	'flags': abuse,
	'flagged_words': bank,
	'score': score,
	'keywords': keywords	
	}

## TWITTER KEYS
#API Key: MqoUC5kAI8mtm5HQNBtp4FgSQ
#API Secret Key lR6V3ZcqemAsa0tlmjjN4OVNAjXTg1SDFcuYcXmPL0QHyT68dV
#Bearer token: AAAAAAAAAAAAAAAAAAAAAKuVIwEAAAAAMsicGY0L1kTAhybeCj%2B8gE4Tpwk%3Dz6rFwfmqnqcnnMcm0KSWVK4pALS0yeE65K5LVfPlnwNjo8nliQ
# credibility algorithhm

# how to define credibility
# - verification -- NO
# - number of times user is flagged -- YES
# - compiling list of whether user is using mostly opinion vs fact based writing
# - how long user has been a member -- maybe
# - number of retweets and likes -- idk about this? NOO
# - user affiliates -- im not sure if this is good either, could lead to sketchhy profiling NOO
# - database of potentially sketchy information cross reference
# - related information section

# how these parameters work
	# user will be either be rewarded or marked down based on twitter usage
	# im thinking we can calculate it as a percentage so its fair for all people
	# for example verified peeps will have a higher denominator to calc from 
	# i.e. verified #/200 and nonverified #/100
	# im hoping to do this as a gpa calculator where each catgory is a percentage and 
	# we add them up to determine final grade

# FUNCTIONS WE NEED

# determine user flags and return score
	# determine if user has been flagged for abuse
	# determine if they send hate speech, racist / sexist comments
	# this will bring down user score
	# score each flag 
	# would be based on twitter's discretion
# score weight up to: _____

# determine fact vs opinion writing
	# can take avg of how much user uses opinion vs fact based writingn
	# comparing the averages, determine score 
	# its gonna be hard to determine fact vs opinon based writing, 
	# well need to research more apis to help us here
	# how do we take into account like normally 
	# can find api that distinguishes how many logical fallacies a person has
	# implement a fact checker? 
	# score weight up to: _____


# INPUT
import json
import requests
from textblob import TextBlob

msg = input('tweet\n')

# # establish categories
# API_KEY = 'hcTLxGHqcQXqTZNHCEnzywEfvHuKDWbJ' 

# def analyze():
# 	params = {
# 		'appid': API_KEY,
# 	}

# 	response = requests.get('http://api.hatebase.org/4-4/authenticate', params)

# 	if response.status_code == 200: # Status: O
# 		print('here')
# 		print(response)
# 	data = response.json()
# 	print(data)
# 		# TODO: Extract the temperature & humidity from data, and return as a tuple
# 	#     return 0

# 	# else:
# 	#     print('error: got response code %d' % response.status_code)
# 	#     print(response.text)
# 	#     return 0.0, 0.0

#Determine user subjectivity
blob = TextBlob(msg)
opinions = blob.subjectivity
extreme = blob.polarity
keywords = blob.noun_phrases

# assign weighted scores to each flag
flags = {
	'not_interest': '',
	'spam': {'fake': '', 'phish': '', 'hashtags': '', 'reply': '', 'else': ''},
	'abusive': {'disrespectful': '', 'private': '', 
		'harassment': '', 'direct_hate': '', 'threatening': '', 'self_harm': ''},
	'misleading': {'false_info': '', 'suppress': '', 'misrepresents': ''},
	'self_harm': '',
}

# keyword phrases
 



# OUTPUT
# final score and json file with percentages in each category
# response text

if __name__ == '__main__':
	print(opinions)
	print(extreme)
	print(nouns)

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
	# score weight up to: ____
	
import json
import requests
from textblob import TextBlob

msg = input('tweet\n')

#Determine user subjectivity
blob = TextBlob(msg)
opinions = blob.subjectivity
extreme = blob.polarity
keywords = blob.noun_phrases # keyword phrases

# assign weighted scores to each flag 
flags = {
	'not_interest': 0,
	'spam': {'fake': '', 'phish': '', 'hashtags': '', 'reply': '', 'else': ''},
	'abusive': {'disrespectful': '', 'private': '', 
		'harassment': '', 'direct_hate': '', 'threatening': '', 'self_harm': ''},
	'misleading': {'false_info': '', 'suppress': '', 'misrepresents': ''},
	'self_harm': '',
}


 



# OUTPUT
# final score and json file with percentages in each category
# response text

## TWITTER KEYS

#API Key: MqoUC5kAI8mtm5HQNBtp4FgSQ

#API Secret Key lR6V3ZcqemAsa0tlmjjN4OVNAjXTg1SDFcuYcXmPL0QHyT68dV

#Bearer token: AAAAAAAAAAAAAAAAAAAAAKuVIwEAAAAAMsicGY0L1kTAhybeCj%2B8gE4Tpwk%3Dz6rFwfmqnqcnnMcm0KSWVK4pALS0yeE65K5LVfPlnwNjo8nliQ

if __name__ == '__main__':

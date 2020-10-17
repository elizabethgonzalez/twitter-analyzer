# credibility algorithhm

# how to define credibility
# - verification
# - number of times user is flagged
# - compiling list of whether user is using mostly opinion vs fact based writing
# - how long user has been a member
# - number of retweets and likes -- idk about this?
# - user affiliates -- im not sure if this is good either, could lead to sketchhy profiling

# how these parameters work
	# user will be either be rewarded or marked down based on twitter usage
	# im thinking we can calculate it as a percentage so its fair for all people
	# for example verified peeps will have a higher denominator to calc from 
	# i.e. verified #/200 and nonverified #/100
	# im hoping to do this as a gpa calculator where each catgory is a percentage and 
	# we add them up to determine final grade

# FUNCTIONS WE NEED

# determine if user is verified & return score
	# users wil not be penalized for not being verified
	# JK MAYBE NOT
# score weight up to: ______

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

# determine user membership age
	# this will be worth little, but longer members will have higher score
	# im thinking we can trust members who have been members longer 
	# determine if a bot as well 

# 


# OUTPUT

# final score and json file with percentages in each category
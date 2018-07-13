import tweepy
import sys
import time
#mainmanu
while True:
	print("1.Retrieve Tweets")
	print("2.Count the followers")
	print("3.Determine the sentiment")
	print("4.Determine location,language and time zone.")
	print("5.Compare tweets ")
	print("6.Analyze top usage ")
	print("7.Tweet a message")
	print("8.exit")
	choice=int(input("enter any choice"))
	consumer_key='aZmCuSveMsQns8xcCDxPKWOpM'
	consumer_secret='VDfUcFFtYQ6kwk5YFGZByGc4ZieNjFlyG3fhZFYC5vzZsr43Cy'
	access_token='1017636237346246656-Kk3xlb2TQNTVAj7SBJ6sr4LigGRBOx'
	access_token_secret='zwDqN2N5Xs02XpjRz1Ph6QB3sqgti8X9ljikh60QlcJMv'
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api=tweepy.API(auth)
	def Retrieve_Tweets():
		user_search=input("enter any hash tag search: ")
		tweets=api.search(user_search,lang="en",count=5,tweet_mode="extended")
		#print(tweets)
		for tweet in tweets:
			print("--------------")
			print(tweet.full_text)
			print("--------------")
	def Count_the_followers():
		user_id=input("enter any id to count the follower:" )
		user=api.get_user(user_id)
		print(user.screen_name)
		print(user.friends_count)
		return
	def Determine_the_sentiment():
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token,access_token_secret)
		api = tweepy.API(auth)
		username=input("enter any user id:")
		tweets = api.user_timeline(screenname=username, count=20)
		tmp = []
		tweets_for_csv = [tweet.text for tweet in tweets]
		for j in tweets_for_csv:
			tmp.append(j)
		pos = 0
		neg = 0
		neu = 0
		print(tmp)
		from paralleldots import set_api_key,get_api_key,sentiment
		set_api_key("2S3zRrv1jxndgO6NQ989I4iJlEU8PHD1aOaAvCM4kw8")
		get_api_key()
		for  t in tmp:
			a = sentiment(t)
			if a['sentiment'] == 'positive':
					pos += 1
			if a['sentiment'] == 'negative':
					neg+= 1
			if a['sentiment'] == 'neutral':
					neu+= 1
		if (pos > neg) and (pos > neu):
				print("postive")
		if (neg > neu) and (neg > pos):
				print("negative")
		if (neu > neg) and (neu > pos):
					print("neutral")
	def Determine_location_language_and_timezone():
		user_id = input("enter the any id to see location:")
		user = api.get_user(user_id)
		print("location:",user.location)
		print("time_zone:",user.time_zone)
		print("language:",user.langs)
	def Compare_tweets():
			user_id = input("enter 1st id Count the compare:")
			user = api.get_user(user_id)
			a1= user.followers_count
			user_id1 = input("enter 2nd id to compare:")
			user1 = api.get_user(user_id1)
			a2 = user1.followers_count
			if a1>a2:
				print("{} is the best user of twitter".format(user.name))
			else:
				print("{} is the best user of tweeter".format(user1.name))
	def Analyze_top_usage():
		status=input("enter any status")
		user_id=input("enter any id to upload the status:")
		api.update_status(status,user_id)
	def Tweet_a_message():
		user_id=input("enter the id to send message:")
		message=input("enter any massage:")
		api.send_direct_message(user=user_id,text=message)	
	if choice==1:
		Retrieve_Tweets()
	if choice==2:
		Count_the_followers()
	if choice==3:
		Determine_the_sentiment()
	if choice==4:
		Determine_location_language_and_timezone()
	if choice==5:
		Compare_tweets()
	if choice==6:
		Analyze_top_usage()
	if choice==7:
		Tweet_a_message()
	if choice==8:
		exit()
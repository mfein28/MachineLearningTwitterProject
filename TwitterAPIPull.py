import tweepy
import csv
from tweepy import OAuthHandler

ckey = 'XmGJg5YuU4bS8F8LdUoCTxPSp'
csecret = 'B4Bp2xVhPz7HZC3O71CmcvFo57k7l6ToTEhT3Aewi3srqqCWrG'
atoken = '2456534122-xGxnlevtZHSW3ZMhXV1s8l7obR1hCPfVHzS8Aiw'
asecret = '4A87PvxzdzxqTuvoWdLZqHIkW6KtcEWIHAHrJx0T5xEPf'
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth, wait_on_rate_limit=True)


class PullTweets():

    def UserTimelinePull(self):
        handle = input("Enter a twitter handle to create CSV for that User:\n")
        print('handle:', handle)
        testTweet = tweepy.Cursor(api.user_timeline, tweet_mode='extended', id=handle, count=200).items(100)
        i = 0
        for tweet in testTweet:
            row = []
            # UserLocation
            userLocation = tweet.user.location
            row.append(userLocation)
            # UserDescription
            userDescription = tweet.user.description
            if (userDescription == ''):
                userDescription = 'N/A'
            row.append(userDescription)
            userLang = tweet.user.lang
            row.append(userLang)
            # TweetLanguage
            tweetLang = tweet.lang
            row.append(tweetLang)
            # TweetText
            tweetText = tweet.full_text
            row.append(tweetText)
            # TweetClientName
            tweetSource = tweet.source
            row.append(tweetSource)
            isVerified = tweet.user.verified
            row.append(isVerified)
            i = i + 1

            with open('mattTest.tsv', 'a') as csvFile:
                writer = csv.writer(csvFile, delimiter='\t')
                writer.writerow(row)
                csvFile.close()
        print(i, " tweets added to CSV file!")

    def tweetTextOnly(self):
        raw_query = input("Enter a query to pull from Twitter: ")
        print(raw_query)
        queryTweets = tweepy.Cursor(api.search, q=raw_query, tweet_mode='extended', result_type="recent",
                                    lang="en").items(500)
        x = 0
        while x < 500:
            for tweet in queryTweets:
                row = []
                tweetText = tweet.full_text
                row.append(tweetText)
                # row.append(0)
                with open('March27encodeTest-noah.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    csvFile.close()
            x = x + 1
        print(x, " tweets added to CSV file!")

    def queryPull(self):
        raw_query = input("Enter a query to pull from Twitter: ")
        print(raw_query)
        with open('March27EncodeTest-noah.csv', 'a') as csvFile:
            row = ['UserLocation', 'AccountLanguage', 'TweetLanguage', 'TweetText', 'TweetClient', 'isVerified',
                   'isMalicious']
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()
        queryTweets = tweepy.Cursor(api.search, q=raw_query, tweet_mode='extended', result_type="recent",
                                    lang="en").items(500)
        x = 0
        while x < 500:
            for tweet in queryTweets:
                row = []
                # UserLocation
                userLocation = tweet.user.location
                if (userLocation == ''):
                    row.append('N/A')
                else:
                    row.append(userLocation)
                # UserDescription
                userDescription = tweet.user.description
                if (userDescription == ''):
                    row.append('N/A')
                else:
                    row.append(userDescription)
                userLang = tweet.user.lang
                row.append(userLang)
                # TweetLanguage
                tweetLang = tweet.lang
                row.append(tweetLang)
                # TweetText
                tweetText = tweet.full_text
                row.append(tweetText)
                # TweetClientName
                tweetSource = tweet.source
                row.append(tweetSource)
                isVerified = tweet.user.verified
                row.append(isVerified)
                row.append(0)

                with open('March27EncodeTest-noah.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                    csvFile.close()
            x = x + 1
        print(x, " tweets added to CSV file!")

    def listPull(self):
        handle = input("Enter a twitter list to create CSV for that list:\n")
        owner = input("Enter the owner's handle for the list: ".format(handle))
        listTweets = tweepy.Cursor(api.list_timeline, tweet_mode='extended', owner_screen_name=owner, slug=handle,
                                   count=200).items(1500)
        x = 0
        for tweet in listTweets:
            row = []
            # UserLocation
            userLocation = tweet.user.location
            row.append(userLocation)
            # UserDescription
            userDescription = tweet.user.description
            row.append(userDescription)
            userLang = tweet.user.lang
            row.append(userLang)
            # TweetLanguage
            tweetLang = tweet.lang
            row.append(tweetLang)
            # TweetText
            tweetText = tweet.full_text
            row.append(tweetText)
            # TweetClientName
            tweetSource = tweet.source
            row.append(tweetSource)
            isVerified = tweet.user.verified
            row.append(isVerified)
            row.append(0)
            x = x + 1

            with open('April5ListPull.tsv', 'a') as tsvFile:
                writer = csv.writer(tsvFile, delimiter='\t', lineterminator='\n')
                writer.writerow(row)
                tsvFile.close()
        print(x, " tweets added to CSV file!")


end_process = 0
run = PullTweets()
while (end_process < 10):
    response = int(input("1: Pull a user timeline tweets\n2: Pull a list of tweets\n3: Pull a search query\n4: Pull tweet text from query\n5: quit\nSelection: "))
    end_process += 1
    if (response is 1):
        run.UserTimelinePull()
    elif (response is 2):
        run.listPull()
    elif (response == 3):
        run.queryPull()
    elif (response == 4):
        run.tweetTextOnly()
    elif (response == 5):
        quit()

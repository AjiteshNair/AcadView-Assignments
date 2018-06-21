
import tweepy
 
#Question 1
print("\n\nQ1.\n")

print("An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread.")
    
consumerKey = "gjD1MsIqRXsAuGSB0O9oNrWMc"       #storing consumerkey from the created api
consumerSecret = "7fAyJ1AakLFKPNItFPmN6lSYF3b7T7zXPzhNC8Qy4CBqvPQbFn"           #storing consumersecret from the created api
  
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)#checking for authorization
auth.secure=True
auth_url = auth.get_authorization_url() #to get url
   
print("Link for authorizing : ",auth_url)

pin = input("Enter The Authorization PIN:")
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens","w")
accessTokenFile.write(token[0]+'\n')
accessTokenFile.write(token[1]+'\n')
print("Now you can check your access token file!!")



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 2
print("\n\nQ2.\n")

print("nslookup www.google.com : 172.217.166.110")
print("nslookup www.facebook.com : 157.240.16.35")
print("nslookup www.twitter.com : 104.244.42.193")


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 3
print("\n\nQ3.\n")

consumer_key = "gjD1MsIqRXsAuGSB0O9oNrWMc"
consumer_secret = "7fAyJ1AakLFKPNItFPmN6lSYF3b7T7zXPzhNC8Qy4CBqvPQbFn"
access_key = "3305131963-fchUQFkUT09qBc5xdAxers4ed5tr6K3i3abM7EH"
access_secret = "rts7WJE4whEplmKP66165WWlGVTVp94QhXpqHmmdb2YCT"
 
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        for i in tmp:
            print(i)
 
 
  # Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("@realDonaldTrump")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



#Question 4
print("\n\nQ4.\n")

print("A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)")
print("\n\nAn API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)")



#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 5
print("\n\nQ5.\n")
#no idea of this will work , didnt get how to extract a song
eden_url="spotify:artist:s23mkadfkwnmosawindjabfaahvashkj"  #this the id used is of my account , code source:documentation.
spotify=spotipy.Spotify()
results=spotify.artist_albums(eden_url,album_type="album")
albums=results['items']

while results['next']:
    results=spotify.next(results)
    albums.extend(results['items'])
    
for album in  albums:
    print((album['name']))


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

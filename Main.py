import tweepy
import discord
token_didi = ""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
bearer = '' 

#Mogfrat
#chapitre 



def home_time():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    home()


def see_tweet_by_specific_user():
    name = input("Enter name of user who are u looking for (@name) :\n")
    specific_user_timeline = api.user_timeline(name)
    for twb in specific_user_timeline:
        print(twb.text)
    home()
    


def post_tweet():
    Mog = "a"
    ms = ""
    ms = input('Enter ur tweet \n')
    api.update_status(status=ms)
    while Mog == "a":
        continu = input("Do u want continue ? Y/N \n").lower
        if continu == "y":  
            post_tweet()
        elif continu == "":
            print("Pls fill answer")
        else:
            home()


def get_information_about_user():
    name = input('Enter name of user who are u looking for (@name) : \n')
    info = api.get_user(name)
    print(info)
    home()


def verif_credential():
    cred = api.verify_credentials()
    print(cred)
    home()


def update_pic_profile():
    filename = input("Enter file location : \n")
    api.update_profile_image(filename)
    home()


def update_background_pic():
    filename = input("Enter file location : \n")
    api.update_profile_background_image(filename)
    home()

def update_profile():
    name = input("Name (20 characters max)\n")
    url = input('Url (100 characters max)\n')
    location = input("Location (30 characters max)\n")
    description = input("Description (160 characters max)\n")
    api.update_profile(name, url, location, description)
    home()


def trends_place():
    loc = input("Local \n")
    trends = api.trends_place(loc)
    for trend in trends:
        print(trend)


def place_val():
    place_val = api.trends_available()
    print(place_val)


def autre():
    choix = "b"
    while choix == "b":
        choix = int(input("What do u want to do ? \n 1.Update profile pic \n 2.Update background pic \n 3.Update profile \n 4.Value of place ( Print a Yahoo! Where On Earth ID of place) \n 5.Trends place(Enter Yahoo! Where On Earth ID for see trends about place)\n"))
        if choix == "":
            print("Your answer don't be empty")
            choix = "a"
        elif choix <1 or choix >6 :
            print("Choose numbers which are display")
            choix = "a"
        elif choix == 1:
            update_pic_profile()
        elif choix == 2:
            update_background_pic()
        elif choix == 3:
            update_profile()
        elif choix == 4:
            place_val()
        elif choix == 5:
            trends_place()
        

def home():
    choix = "a"
    while choix == "a":
        choix = int(input("What do u want to do ? \n 1.See Actuallity \n 2.See tweet by specific user \n 3.Get informations about a user\n 4. See credential of bot. \n 5.Post a tweet \n 6. The rest"))
        if choix == "":
            print("Your answer don't be empty")
            choix = "a"
        elif choix <1 or choix >6 :
            print("Choose numbers which are display")
            choix = "a"
        elif choix == 1:
            home_time()
        elif choix == 2:
            see_tweet_by_specific_user()
        elif choix == 3:
            get_information_about_user()
        elif choix == 4:
            verif_credential()
        elif choix == 5:
            post_tweet()
        elif choix == 6:
            autre()
            

home()

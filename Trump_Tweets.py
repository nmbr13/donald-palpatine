import requests
from bs4 import BeautifulSoup
import datetime
import time


replace_word = {
    'Border':'Rebel Base',
    'border':'Rebel Base',
    "Russian's":"Eewok's",
    "Prime Minister" : "Senate Vicroy",
    'Putin': 'Grand Moff Putin',
    'Obama':'Mace Windu',
    'Dems':'Wookiees',
    'left':'Wookies',
    'Leftists':'Wookies',
    'Democrates' : 'Wookiees',
    'Democrat':'Wookiee',
    'REPUBLICANS':'Rebel Scum',
    'Republicans':'Rebel Scum',
    'Conservatives' : 'Clone Troopers',
    'conservatives' : 'Stormtroopers',
    'Right Wing':'Stormtroopers',
    'President': 'Galactic Emperor',
    'Donald':'',
    'Trump':'Palpatine',
    'Senate':'Galactic Senate',
    'Congress' : 'The Galactic Senate',
    'Army':'Clones',
    'army':'Clones',
    'Armed Forces':'Clone Army',
    'armed forces':'Clone Army',
    'Marine':'Clone Trooper',
    'Vietnam':'the Battle of Gionosis',
    'Military':'Clone Army',
    '@FoxNews':'The Jedi Counsil',
    'Russia':'Ice Planet Hoth',
    'North Korea':'Mustafar',
    'China':'Tatooine',
    'Wall': 'Death Star',
    'WALL': 'Death Star',
    'money':'sum of Republic Credits',
    'Senator':'Chancellor',
    'Mexico':'Jakku',
    'FBI':'Eewoks',
    'DOJ':'Mandalorians',
    'Oval Office':'Black Vacuum of Space',
    'the Middle East':'Tatooine',
    "The Middle East":'Tatooine',
    'Election Day':'Blowing Up Alderane',
    'elections':'blowing up Alderane',
    'America':'Galactic Empire',
    'the Election':'we blew up Alderane',
    'Hillary':'Padmay',
    'Clinton':'Skywalker',
    'got elected':'took over the Galactic Senate',
    'administration':'galactic reign',
    'Administration' : 'galactic reign',
    'country':'star system',
    'Country' : 'plantary system',
    'Supreme Court':'Sith Council',
    'nukes':'lightsabers',
    'fight': 'lightsaber duel',
    'fake news':'Rebel Propoganda',
    'FAKE NEWS':'Rebel Propoganda',
    'Fake News':'Rebel Propoganda',
    'White House':'Sith Counsel',
    'world':'Galaxy',
    'World' : 'Galaxy',
    'files':'transmissions',
    'documents':'transmissions',
    'radical':'rogue',
    'Radical':'Rogue',
}

def trump_tweets(n):
    tweet_log = {}
    url  = 'https://twitter.com/realDonaldTrump'
    r = requests.api.get(url)
    t = r.text
    soup = BeautifulSoup(t, 'html.parser')
    tweet = soup.find_all('p', attrs={'class':'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    test_tweets = [t.text for t in tweet][:n]
    store_tweets = test_tweets[:]
#     for item in test_tweets:
#         if 'pic' in item:
#             pass
#         else:
#             store_tweets = store_tweets + [item]

    def replace_all(text):
        for i, j in replace_word.items():
            text = text.replace(i, j)
        return text
    for tweet in store_tweets:
        t1 = replace_all(tweet)
        t2 = tweet
        if t1 == t2:
            store_tweets.remove(tweet)
    current_date = datetime.datetime.now()
    tweet_date = f'{current_date.month}-{current_date.day}-{current_date.year}'
    tweet_list = [{'date': tweet_date,'tweet':replace_all(text)} for text in store_tweets]
    return tweet_list

# Variable : ""

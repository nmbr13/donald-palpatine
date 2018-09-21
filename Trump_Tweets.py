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
    'Democrates' : 'Wookiees',
    'Democrat':'Wookie',
    'Democrats':'Storm Troopers',
    'REPUBLICANS':'Rebel Scum',
    'Republicans':'Rebel Scum',
    'President': 'Galactic Emperor',
    'Donald':'',
    'Trump':'Palpatine',
    'Senate':'Galactic Senate',
    'Congress' : 'The Galactic Senate',
    'Army':'Clones',
    'army':'Clones',
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
}

def trump_tweets():
    tweet_log = {}
    url  = 'https://twitter.com/RealDonad_Trump'
    r = requests.api.get(url)
    t = r.text
    soup = BeautifulSoup(t, 'html.parser')
    tweet = soup.find_all('p', attrs={'class':'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    test_tweets = [t.text for t in tweet][:10]
    def replace_all(text):
        for i, j in replace_word.items():
            text = text.replace(i, j)
        return text
    return [{datetime.datetime.now():replace_all(text)} for text in test_tweets]

import re
import requests
import json
from bs4 import BeautifulSoup

class TooManyRequest(Exception): ...
class NotFound(Exception): ...
class UnknownError(Exception): ...
SONG_PAGE = 'https://hopamchuan.com/song/{SongID}/*'
RYTHM_PAGE = 'https://hopamchuan.com/partial/song_partial/rhythm_vote/{SongID}'
DATA = {'something':'something'}

def get_song_by_id(SongID):
    res = requests.get(SONG_PAGE.format(SongID=SongID))
    if res.status_code==200: soup = BeautifulSoup(res.text,'html.parser')
    elif res.status_code==429: raise TooManyRequest('Too many request')
    elif res.status_code==404: raise NotFound('Not Found This ID')
    else: raise UnknownError('Something wrong!')
    #Get the name
    tags = soup('h1')
    song = tags[0].text.strip()
    #Get the singer
    tags = soup('a') # class="author-item"
    for tag in tags:
        item = tag.get('class')
        if item is None: continue
        elif 'author-item' in item: 
            singer = tag.text.strip()
            tempLst = re.findall('/\d+/',tag['href'].strip())
            singer_id = int(re.findall('\d+',tempLst[0])[0])
    #Get the votes rythm
    res = requests.post(RYTHM_PAGE.format(SongID=SongID),data=DATA)
    if res.status_code==200: soup = BeautifulSoup(res.text,'html.parser')
    elif res.status_code==429: raise TooManyRequest('Too many request')
    elif res.status_code==404: raise NotFound('Not Found This ID')
    else: raise UnknownError('Something wrong!')
    rythm_tags = soup('a')
    rythm = []
    for tag in rythm_tags:
        rythm.append(tag['data-rhythm'])
    votes = soup('div')[0].text.strip()
    votes = re.findall('\d+',votes)
    retdict = dict()
    for index in range(len(votes)):
        retdict[rythm[index]] = int(votes[index])
    rythm = json.dumps(retdict)
    return(SongID,song,singer_id,rythm)
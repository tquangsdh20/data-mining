#!/usr/bin/env python
# coding: utf-8

# ## Scraping Music Part

# ### Define the functions for pre-scraping and generate log

# In[3]:


import os
import os.path
from DBMS import DB
from HopAmChuan import get_song_by_id
from time import sleep

def list2str(lst:list):
    retstr = ''
    for item in lst:
        retstr+=str(item[0])+' '
    return retstr

def trace_log(filename:str):
    if os.path.exists(filename):
        __fh = open(filename)
        logs = __fh.read().split()
        __fh.close()
        os.remove(filename)
    else: logs=[]
    return logs

def generate_log(filename:str,log:str):
    if os.path.exists(filename):
        os.remove(filename)
    fp = open(filename,'w')
    fp.write(log)
    fp.close()

def generate_report(db:DB):
    __users = list2str(db.get_users())
    __songs = list2str(db.get_songs())
    __singers = list2str(db.get_singers())
    generate_log('./logs/users.log',__users)
    generate_log('./logs/songs.log',__songs)
    generate_log('./logs/singers.log',__singers)


# ### Scraping Song

# In[11]:


db = DB('./output/music.db')
generate_report(db)
USER_LOGS = trace_log('./logs/users.log')
SONG_LOGS = trace_log('./logs/songs.log')
SINGER_LOGS = trace_log('./logs/singers.log')

def insert_songs(db:DB,filename):
    fh = open(filename)
    SongList = fh.read().split()
    #db.init_database()  --> Important to remove this line
    log = []
    rcd_cnt = 0
    for SongID in SongList:
        if (SongID in SONG_LOGS) or (SongID in log) : continue
        try:
            record = get_song_by_id(SongID)
            log.append(SongID)
            sleep(0.5)
        except:
            pass
        else:
            rcd_cnt+=1
            db.insert_song(record)
            if rcd_cnt%50==0: db.commit()
    generate_report(db)

#Insert new user and insert all song in file --> User's playlist + Insert all songs into DBMS
def insert_new_user(db:DB,username:str,file:str):
    if username in USER_LOGS: 
        print('The username exists')
        return False
    if os.path.exists(file):
        fh = open(file)
        SongList = fh.read().split()
        playlist = ''
        for song in SongList:
            playlist += str(song) + ' '
    else:
        print(f'File "{file}" doesn\'t exist')
        return False
    db.insert_user((username,playlist))
    insert_songs(file)
    return True


# ### Insert songs with StartID to EndID

# In[ ]:


def insert_songs_by_range(db:DB,startID:int,endID:int):
    SongList = range(startID,endID+1)
    #db.init_database()  --> Important to remove this line
    log = ''
    rcd_cnt = 0
    for SongID in SongList:
        if (str(SongID) in SONG_LOGS): continue
        print(SongID)
        try:
            record = get_song_by_id(SongID)
            sleep(0.5)
        except:
            log += str(SongID) + ' '
            pass
        else:
            rcd_cnt+=1
            db.insert_song(record)
            if rcd_cnt%20==0: db.commit()
    if not os.path.exists('./logs'):
        os.makedirs('./logs')    
    generate_log('./logs/failures.log',log)
    db.commit()


# In[ ]:
# 14126

insert_songs_by_range(db,4000,5000)
db.close()





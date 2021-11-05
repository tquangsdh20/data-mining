#!/usr/bin/env python
# coding: utf-8

# ## Data Mining Project
# 
# ### Import essential library

# In[1]:


import os
import json
from DBMS import DB


# ### Define the functions and constants for SQL Query with music database

# In[14]:


# Connecting to music database without calling initial function again
db = DB('./output/music.db')

# Define the constants for QUERY statement
GET_PLAYLIST_BY_USERNAME = """SELECT playlist FROM user WHERE name = ? LIMIT 1;"""
GET_PLAYLIST_BY_USER_ID = """SELECT playlist FROM user WHERE id = ? LIMIT 1;"""
GET_RYTHM_BY_SONG_ID = """SELECT id,rythm FROM song WHERE id = ? ;"""


# ### Query and Get the playlist with UserID = 39

# In[10]:


choice = input('''Analysis by UserID or UserName?
    1. Username
    2. UserID
Enter your choice: ''')
if choice == '1':
    text = 'Please enter the user name for analysis: '
    user = input(text)
    db.cur.execute(GET_PLAYLIST_BY_USERNAME,(user,))
    playlist = db.cur.fetchone()[0]
elif choice == '2':
    text = 'Please enter the UserID for analysis: '
    user = input(text)
    db.cur.execute(GET_PLAYLIST_BY_USER_ID,(user,))
    playlist = db.cur.fetchone()[0]
else:
    print('Invalid choice!')
    exit()
songs = playlist.split()


# ### Query and Get the songs in playlist

# In[20]:


rythms = []
names = []
for song in songs:
    db.cur.execute(GET_RYTHM_BY_SONG_ID,(song,))
    rythm = db.cur.fetchone()
    if rythm is None: continue
    rythms.append(rythm[1])
    names.append(rythm[0])


# ### Convert string to dictionary of rythm votes

# In[16]:


votes = []
for rythm in rythms:
    vote = json.loads(rythm)
    votes.append(vote)


# ### Convert all votes to rows

# In[18]:


rows = []
head = 'song' + ','
# devguy97: update keys list for keeping correctly position values
keys = []
for key in votes[0].keys():
    head += key + ','
    keys.append(key)
rows.append(head.strip())

cnt = 0
for vote in votes:
    row = str(names[cnt]) + ','
    cnt+=1
    # devguy97: update value of dictionary follow the key position of header
    for key in keys:
        row += str(vote[key]) + ','
    rows.append(row.strip())


# ### Write all rows to file text

# In[19]:


with open('./output/'+user+'.txt','wb') as fp:
    for row in rows:
        fp.write(((row+'\n').replace(',\n','\n')).encode())


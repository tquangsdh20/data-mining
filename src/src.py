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

def main():
    SONG_LOGS = trace_log('./logs/songs.log')
    USER_LOGS = trace_log('./logs/users.log')
    SINGER_LOGS = trace_log('./logs/singers.log')
    fh = open('song.txt')
    SongList = fh.read().split()

    db = DB('Music.db')
    db.init_database()
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
    db.close()

def export_table(user_id):

    return

main()
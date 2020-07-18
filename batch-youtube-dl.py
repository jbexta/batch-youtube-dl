import csv
import sys
import youtube_dl
import queue

config_dir = '<PATH-TO-CONFIG-DIRECTORY>'
video_dir = '<PATH-TO-VIDEO-DIRECTORY>'

ydl_queue = queue.Queue

ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio',
    'outtmpl': '',
    'download_archive': config_dir + '/archive',
    'restrictfilenames': True,
    'ignoreerrors': True
}

outtmpl_groups = {
    '$channel': video_dir + '/%(playlist_uploader)s/%(playlist_title)s/%(title)s.%(ext)s',
    '$playlist': video_dir + '/%(playlist_uploader)s/%(playlist_title)s/%(title)s.%(ext)s',
    '$single': video_dir + '/(%(playlist_uploader)s)_%(playlist_title)s/%(title)s.%(ext)s',
    '$liked_videos': video_dir + '/%(playlist_uploader)s/Liked_videos/%(title)s.%(ext)s'
}

batch_csv = config_dir + '/batch.csv'

with open(batch_csv, newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        row_url = row['url']
        row_outtmpl = row['outtmpl']

        if row_outtmpl.startswith('$'):
            ydl_opts['outtmpl'] = outtmpl_groups[row_outtmpl]
        else:
            ydl_opts['outtmpl'] = row_outtmpl

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
               ydl_queue.put(ydl.download([row_url]))
        except:
            e = sys.exc_info()[0]
            print("//Error: %s" % e)

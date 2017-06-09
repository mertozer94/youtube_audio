from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

# --download-archive for only new videos

ydl_opts = {
    'format': 'best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'ignoreerrors': True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=CIvtiNpKEY0'])
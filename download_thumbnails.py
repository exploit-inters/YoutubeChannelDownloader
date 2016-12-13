import bot
import os
import traceback
import ycdl
import ytapi

from voussoirkit import downloady

youtube_core = ytapi.Youtube(bot.YOUTUBE_KEY)
youtube = ycdl.YCDL(youtube_core)

DIRECTORY = 'C:\\users\\owner\\youtube thumbnails'

videos = ycdl_repl.youtube.get_videos()
for video in videos:
    try:
        thumbnail_path = os.path.join(DIRECTORY, video['id']) + '.jpg'
        if os.path.exists(thumbnail_path):
            continue
        result = downloady.download_file(video['thumbnail'], thumbnail_path)
        print(result)
    except Exception as e:
        traceback.print_exc()

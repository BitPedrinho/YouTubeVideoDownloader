from pytubefix import YouTube
from pytubefix.cli import on_progress

url = 'https://www.youtube.com/watch?v=TmIwm5RElRs'

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.filter(resolution="360p")
ys.download(r'c:\Users\resti\Downloads')
#Script para baixar para baixar vídeos do Yotube.
from pytube import YouTube, streams
url = str(input('Insira a URL do vídeo: '))
video = YouTube(url)
baixarvideo = video.streams.get_highest_resolution()
baixarvideo.download()
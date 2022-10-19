#YouTube Video Downloader
############################################
#Author: Cole Hamilton
#Date: 10/18/2022
#Version: 1.0
#Description: This script will download a YouTube video
#%pip install pytube
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=Bt3KLEetP1Y")
mp4_files = yt.streams.filter(file_extension = "mp4")
mp4_369p_files = mp4_files.get_by_resolution("360p")
mp4_369p_files.download("/Users/cole/Library/CloudStorage/OneDrive-Personal/Coraline")
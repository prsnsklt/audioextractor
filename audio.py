import moviepy.editor
import os
import re


#Inserting video from your working directory
video=moviepy.editor.VideoFileClip("VID_20191001_121651.mp4") 

#extreaction audio
audio=video.audio

#writing the audio file
audio.write_audiofile('1.mp3')
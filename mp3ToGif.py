from moviepy.editor import *

video = VideoFileClip("video.mp4")
video.write_gif("final.gif")
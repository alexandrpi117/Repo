from moviepy.editor import *
video=moviepy.editor.VideoFileClip("some.mov")
audio=video.audio()
audio.write_audiofile("new_audio.mp3")

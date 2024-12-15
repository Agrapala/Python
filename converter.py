import moviepy.editor
c_n = moviepy.editor.VideoFileClip("12.mp4")
e_n = c_n.audio
e_n.write_audiofile("audio.mp3")

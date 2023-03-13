import moviepy.editor

video_name = input("Write video-file name: \n")
audio_name = f"{video_name[:-3]}.mp3"

video = moviepy.editor.VideoFileClip(video_name)

audio = video.audio
audio.write_audiofile(audio_name)
print(f"Audio written to file: {audio_name}")

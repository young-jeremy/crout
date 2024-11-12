"""def create_subtitle_clips(subtitles, videosize, fontsize=24, font='Arial', color='yellow', debug=False):
    subtitle_clips = []
    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time-start_time

        video_width, video_height = videosize
        text_clip = TextClip(subtitle.text, bg_color='black', font=font, fontsize=fontsize, size=(video_width*3/4, None), methods='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height*4/5
        text_position = (subtitle_y_position, subtitle_x_position)
        subtitle_clips.append(text_clip.set_position(text_position))
        return subtitle_clips
    video = VideoFileClip()


text = "Your transcribed text"
subtitle_duration = 5  # Adjust as needed
text_chunks = [text[i:i + subtitle_duration] for i in range(0, len(text), subtitle_duration)]

start_time = 0
for i, chunk in enumerate(text_chunks):
    end_time = start_time + subtitle_duration
    subtitle = TextClip(chunk, fontsize=24, color='white')
    subtitle = subtitle.set_position(('center', 'bottom')).set_duration(subtitle_duration)
    subtitle = subtitle.set_start(start_time)
    subtitle.write_videofile(f'subtitle_{i}.mp4', codec='libx264')
    start_time = end_time

with sr.AudioFile('video_audio.wav') as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)  # You can use other engines
    print("Transcription: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


video = VideoFileClip(video_path)
subtitles = [VideoFileClip(f'subtitle_{i}.mp4') for i in range(len(text_chunks))]

final_video = video.set_duration(sum([subtitle.duration for subtitle in subtitles]))
final_video = final_video.set_audio(audio_clip)

for subtitle in subtitles:
    final_video = final_video.set_duration(subtitle.duration)
    final_video = final_video.set_duration(subtitle.duration)
    final_video = final_video.set_duration(subtitle.duration)

final_video.write_videofile('video_with_subtitles.mp4')"""
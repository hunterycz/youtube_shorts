# youtube_shorts
Create YouTube Shorts using AI that is completely automated! Process of taking engaging background videos from youtube, taking stories from reddit or AI generated, adding some background music, and overlaying it all together to create AI Masterpieces.

# Files
1) downloader.py: Used to take youtube videos and convert them to either mp3 or mp4 formats and save them into the "background_video" or the "background_music" directories

2) text2audio: Utilizes the API from the website "ElevenLabs" that will take text to convert into audio. Once text is enterted into the function it will make a API request with the text and return it in audio form and save it to the "stories_audio" directory

# Directories:
1) background_music: Holds all music used for the background of generated videos
2) background_video: Holds all the engaging videos used for interest in the background of the generated videos
3) completed_videos: Holds all completed videos for content
4) stories: Holds all reddit/AI generated stories in .txt format
5) stories_audio: Holds all the reddit/AI generated stories in a mp3 converted audio format

# Dependencies/Libraries
1) pytube
2) python-dotenv
3) elevenlabs
4) moviepy
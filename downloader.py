# imports
import os
from pytube import YouTube

# directory paths
MAIN_DIR = os.getcwd()
PATH_TO_BACKGROUND_VIDEOS = os.path.join(MAIN_DIR, "background_video")
PATH_TO_BACKGROUND_MUSIC = os.path.join(MAIN_DIR, "background_music")


class Video:
    '''
    Class to grab youtube videos with other functionalities
    such as "video_info" and "downloader."

    Methods:
        video_info: Returns a dictionary of info
                    from the youtube video url
        downloader: Returns a mp4 file of the youtube
                    video url used to find the video
    '''

    def __init__(self, url: str):
        self.url = url
        self.yt = YouTube(url)

    def video_info(self) -> dict:
        try:
            # create a info dictionary with
            # the youtube video stats and information
            info = {
                "author": self.yt.author,
                "title": self.yt.title,
                "thumbnail_url": self.yt.thumbnail_url,
                "description": self.yt.description,
                "video_statistics": {
                    "length": self.yt.length,
                    "date_released": self.yt.publish_date,
                    "views": self.yt.views
                }

            }

            # return the info dictionary
            return info
        except Exception as e:
            return f"Error Occurred: {e}"

    def downloader_mp4(self, save_name: str) -> str:
        try:
            # get video with highest quality
            video = self.yt.streams.filter(
                file_extension='mp4',
                only_video=True).order_by('resolution').desc().first()

            if video is None:
                print("No MP4 video available for download.")
                return
            # download the video to the background_video
            # directory with the "saved_name" for the title
            video.download(
                output_path=PATH_TO_BACKGROUND_VIDEOS,
                filename=f"{save_name}.mp4"
            )

            # return a confirmation string
            print(f"Video: {save_name}.mp4 was downloaded successfully!")
            return

        except Exception as e:
            print(f"Error Occurred: {e}")
            return

    def downloader_mp3(self, save_name: str) -> str:
        try:
            # get video with only the audio
            audio_stream = self.yt.streams.filter(only_audio=True).first()

            if not audio_stream:
                print("No Audio stream available for this video.")
                return

            # download the audio_stream
            audio_stream.download(
                output_path=PATH_TO_BACKGROUND_MUSIC,
                filename=f"{save_name}.mp3"
            )

            # return a confirmation string
            print(f"Audio: {save_name}.mp3 was downloaded successfully!")
            return

        except Exception as e:
            print(f"Error Occurred: {e}")
            return


if __name__ == "__main__":
    while True:
        # prompt the user for the url and
        # the new filename for the video
        url = str(input("Please enter the URL: "))
        file_type = str(input("Is it mp3 or mp4: "))
        save_name = str(input("New Name for the Video: "))

        # create an instance of the Video class with the URL
        vid = Video(url)

        if file_type == "mp4":
            # download the video
            vid.downloader_mp4(save_name)
        elif file_type == "mp3":
            # download the audio
            vid.downloader_mp3(save_name)
        else:
            print("File Type Incorrect Enter Correctly.")

        answer = str(input("Download Another Video? (y/n): ")).lower()
        if answer == 'n':
            break

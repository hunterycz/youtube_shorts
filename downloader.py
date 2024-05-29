# imports
from pytube import YouTube
import os
import time

# directory paths
MAIN_DIR = os.getcwd()
PATH_TO_BACKGROUND_VIDEOS = os.path.join(MAIN_DIR, "background_video")


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

    def downloader(self, save_name: str) -> str:
        try:
            # start the time variable
            start = time.time()

            # get video with highest quality
            video = self.yt.streams.filter(
                file_extension='mp4',
                only_video=True).order_by('resolution').desc().first()

            if video is None:
                return "No MP4 video available for download."
            # download the video to the background_video
            # directory with the "saved_name" for the title
            video.download(
                output_path=PATH_TO_BACKGROUND_VIDEOS,
                filename=f"{save_name}.mp4"
            )

            # end time
            end = time.time()
            # return a string confirming the video
            # was downloaded successfully to the directory
            return f"Video: {save_name}.mp4 was downloaded successfully!\
                     Total Time: {end-start:.2f} seconds"
        except Exception as e:
            return f"Error Occurred: {e}"


if __name__ == "__main__":
    while True:
        # prompt the user for the url and
        # the new filename for the video
        url = str(input("Please enter the URL: "))
        save_name = str(input("New Name for the Video: "))

        # create an instance of the Video class with the URL
        vid = Video(url)

        # download the video
        vid.downloader(save_name)

        answer = str(input("Download Another Video? (y/n): ")).lower()
        if answer == 'n':
            break

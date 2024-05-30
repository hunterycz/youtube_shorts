# imports
import moviepy.editor as mp
import os


def resize_video(input_path, output_path, target_ratio):
    # load the clip
    clip = mp.VideoFileClip(input_path)

    # Get the original video dimensions
    original_width, original_height = clip.size

    # Calculate the target height based on the target aspect ratio
    target_height = int(original_width/target_ratio)

    # Resize the video clip while maintaining the aspect ratio
    resized_clip = clip.resize(height=target_height)

    # Write the resized video clip to the output file
    resized_clip.write_videofile(output_path)


if __name__ == "__main__":
    path_in = os.path.join("background_video", "gta_gameplay.mp4")
    path_out = os.path.join("background_video", "gta_gameplay_resized.mp4")

    resize_video(path_in, path_out, target_ratio=(9/16))

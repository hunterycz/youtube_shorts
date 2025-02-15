# imports
import os
from dotenv import load_dotenv
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Load the environment variables from the .env file
load_dotenv()

# connect the the elevenlabs client using
# our API credentials from the .env file
ELEVENLABS_API_KEY = os.getenv("XI_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY
)


def text_to_speech_file(text: str) -> str:
    '''
    Functions that connects to ElevenLabs API with login
    credentials from the .env file then takes text and sends
    it to ElevenLabs and returns a mp3 audio file to the
    'stories_audio' directory.

    Parameter(s):
        text: string
    '''
    try:
        # Calling the text_to_speech conversion API with detailed parameters
        response = client.text_to_speech.convert(
            voice_id="ErXwobaYiN019PkySvjV",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True
            ),
        )

        # Generate a unique file name for the output MP3 file
        save_file_path = f"stories_audio/{uuid.uuid4()}.mp3"

        # writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        # print to the terminal it was successfull
        print(f"{save_file_path}: A new audio file was saved successfully!")

        # Return the path of the saved audio file
        return save_file_path

    except Exception as e:
        # Handle exceptions here
        print(f"An error occurred: {e}")
        return None


def text_file_exists_checker(file_name: str) -> bool:
    '''
    Checks if the file name exists with in the 'stories' directory

    Parameter(s):
        file_name: string

    Returns:
        bool: True
        bool: False
    '''
    file_path = os.path.join("stories", file_name)

    if not os.path.exists(file_path):
        return False
    else:
        return True

if __name__ == "__main__":
    while True:
        file_to_convert = str(input("Enter File Name from 'Stories' Directory: "))

        if text_file_exists_checker(file_to_convert):
            # now that it exists format it correctly
            txt = format_text_file(file_to_convert)

            # convert it to audio
            text_to_speech_file(txt)

            # break out of the loop
            print("PROGRAM FINISHED")
            print("EXITING NOW....")
            break

        print("File Not Found! Please Enter a Correct File Name.")

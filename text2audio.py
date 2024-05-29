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


# create a function to handle converting
# the text to speech using the client

def text_to_speech_file(text: str) -> str:
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
        save_file_path = f"{uuid.uuid4()}.mp3"

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


if __name__ == "__main__":
    while True:
        # enter the text to generate to audio
        txt = str(input("Enter Text to Convert to Audio: "))

        if not txt:
            print("Please Enter Some Text")
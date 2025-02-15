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

if __name__ == "__main__":

from gtts import gTTS
from pydub import AudioSegment
import os

def sing_lyrics(lyrics, lang='en'):
    tts = gTTS(text=lyrics, lang=lang)
    tts.save("song.mp3")
    song = AudioSegment.from_mp3("song.mp3")
    song.export("final_song.wav", format="wav")
    os.system("start final_song.wav")  # Use "afplay" on Mac or "xdg-open" on Linux

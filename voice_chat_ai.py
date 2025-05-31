import os
import queue
import sounddevice as sd
import vosk
import sys
import pyttsx3
import google.generativeai as genai

# ====== CONFIGURATION ======
API_KEY = "AIzaSyB8YVZz-UYA6ILALFOX1ljdnsYgWLiYE_Q"  # <<< PUT your actual key here
genai.configure(api_key=API_KEY)

# Use 'gemini-1.5-flash' – faster & available
model = genai.GenerativeModel('gemini-1.5-flash')

# ====== TEXT-TO-SPEECH SETUP ======
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# ====== VOSK SETUP ======
vosk_model_path = "D:/omniverse_ai/vosk-model-small-en-us-0.15"
if not os.path.exists(vosk_model_path):
    print("Vosk model not found!")
    sys.exit()

vosk_model = vosk.Model(vosk_model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_audio():
    print("[🎙️ Speak now or press Enter to type]")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(vosk_model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                text = eval(result)['text']
                return text

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

def chat_loop():
    while True:
        print("\nChoose input method:")
        print("1. Type")
        print("2. Voice")
        choice = input("Enter 1 or 2 (or q to quit): ").strip()

        if choice.lower() == 'q':
            break
        elif choice == '1':
            user_input = input("You: ")
        elif choice == '2':
            user_input = listen_audio()
            print("You (voice):", user_input)
        else:
            print("Invalid choice.")
            continue

        if not user_input:
            continue

        print("🤖 Gemini is thinking...")
        response = ask_gemini(user_input)
        print("AI Response:", response)
        speak(response)

if __name__ == "__main__":
    print("=== Omniverse Voice+Chat AI ===")
    chat_loop()


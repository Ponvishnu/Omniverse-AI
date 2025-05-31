import customtkinter as ctk
from PIL import Image, ImageTk
import pyttsx3
import sounddevice as sd
import queue
import vosk
import sys
import os
import json
import threading
import google.generativeai as genai

# Extra Modules
from gtts import gTTS
from pydub import AudioSegment
from diffusers import StableDiffusionPipeline
import torch

# === Gemini Configuration ===
genai.configure(api_key="youe_api_key")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

# === Vosk Model (Offline Speech-to-Text) ===
model_path = "vosk-model-small-en-us-0.15"
if not os.path.exists(model_path):
    print("Download Vosk model and unzip as 'vosk-model-small-en-us-0.15'")
    sys.exit()
vosk_model = vosk.Model(model_path)
q = queue.Queue()

# === TTS Engine ===
engine = pyttsx3.init()

# === Image Generator (Diffusers) ===
def generate_image(prompt, output_path="output.png"):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32)
    pipe = pipe.to("cpu")
    image = pipe(prompt).images[0]
    image.save(output_path)
    chat_display.insert(ctk.END, f"🖼️ Image generated and saved as {output_path}\n")

# === Music Generator (Text to Singing) ===
def sing_lyrics(lyrics, lang='en'):
    tts = gTTS(text=lyrics, lang=lang)
    tts.save("song.mp3")
    song = AudioSegment.from_mp3("song.mp3")
    song.export("final_song.wav", format="wav")
    os.system("start final_song.wav")
    chat_display.insert(ctk.END, "🎶 Singing the lyrics...\n")

# === Video Simulation ===
def simulate_video_creation(prompt):
    generate_image(prompt, "scene.png")
    sing_lyrics("Narrating: " + prompt)
    chat_display.insert(ctk.END, "🎬 Simulated video created with image and narration.\n")

# === GUI Setup ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("640x820")
app.title("Omniverse AI Assistant")

# === Logo ===
logo_image = Image.open("D:/omniverse_ai/Omniverse AI Logo Design.png").resize((100, 100))
logo = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(app, image=logo, text="")
logo_label.pack(pady=10)

# === Chat Display ===
chat_display = ctk.CTkTextbox(app, width=580, height=420, font=("Arial", 14))
chat_display.pack(pady=10)
chat_display.insert(ctk.END, "Welcome to Omniverse AI!\n\n")

# === Text Input ===
entry = ctk.CTkEntry(app, width=520, font=("Arial", 14))
entry.pack(pady=10)

# === Buttons ===
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def generate_response(user_input):
    try:
        chat_display.insert(ctk.END, "Omniverse AI: Thinking...\n")
        chat_display.see(ctk.END)
        response = model.generate_content(user_input)
        reply = response.text.strip()
        chat_display.insert(ctk.END, f"Omniverse AI: {reply}\n")
        chat_display.see(ctk.END)
        threading.Thread(target=speak_text, args=(reply,), daemon=True).start()
    except Exception as e:
        chat_display.insert(ctk.END, f"❌ Error: {e}\n")

def send_input():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    entry.delete(0, ctk.END)
    chat_display.insert(ctk.END, f"You: {user_text}\n")
    chat_display.see(ctk.END)
    threading.Thread(target=generate_response, args=(user_text,), daemon=True).start()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def recognize_speech():
    rec = vosk.KaldiRecognizer(vosk_model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Listening...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    chat_display.insert(ctk.END, f"You (voice): {text}\n")
                    chat_display.see(ctk.END)
                    threading.Thread(target=generate_response, args=(text,), daemon=True).start()
                    break

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

ctk.CTkButton(button_frame, text="💬 Send", command=lambda: threading.Thread(target=send_input, daemon=True).start()).grid(row=0, column=0, padx=10)
ctk.CTkButton(button_frame, text="🎙️ Speak", command=lambda: threading.Thread(target=recognize_speech, daemon=True).start()).grid(row=0, column=1, padx=10)
ctk.CTkButton(button_frame, text="🖼️ Image", command=lambda: threading.Thread(target=lambda: generate_image(entry.get()), daemon=True).start()).grid(row=1, column=0, pady=10)
ctk.CTkButton(button_frame, text="🎵 Sing", command=lambda: threading.Thread(target=lambda: sing_lyrics(entry.get()), daemon=True).start()).grid(row=1, column=1, pady=10)
ctk.CTkButton(button_frame, text="🎬 Video", command=lambda: threading.Thread(target=lambda: simulate_video_creation(entry.get()), daemon=True).start()).grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()

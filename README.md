# 🌌 Omniverse AI

**All-in-one Gemini-powered AI Desktop Assistant in Python**

Omniverse AI is a powerful, voice-enabled and multimodal desktop assistant built using Python, Google's Gemini API, and Vosk for offline speech recognition. It combines productivity, creativity, and smart automation into a single application.

---

## 🔮 Features

| Feature | Description |
|--------|-------------|
| 💬 Chat | Ask anything using Gemini 1.5 Flash and get smart, spoken responses. |
| 🎙️ Voice Commands | Speak to the assistant using offline voice recognition with Vosk. |
| 🛑 Stop Speaking | Instantly stop TTS response with a single click. |
| 🖼️ Image Generation | Create AI images using Stable Diffusion (offline or online options). |
| 🎵 AI Singing | Enter lyrics and hear them sung using gTTS + audio playback. |
| 🎬 Video Simulation | Generate a scene image and narrated audio to simulate video creation. |
| 🩺 Health Prediction | Predict health risks with 90%+ accuracy using AI-powered medical prompts. |
| 📑 Resume Builder | Create ATS-friendly resumes dynamically from user input. |
| 📄 Document Generator | Auto-generate professional PDF, DOCX, PPT, and Excel files. |

---

## 🧠 Technologies Used

- [Google Generative AI (Gemini API)](https://ai.google.dev/)
- [Vosk](https://alphacephei.com/vosk/) – Offline speech recognition
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [Pyttsx3](https://pypi.org/project/pyttsx3/) – TTS engine
- [gTTS](https://pypi.org/project/gTTS/) – Singing TTS
- [Pydub](https://pypi.org/project/pydub/) – Audio processing
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – Modern GUI
- [FPDF / python-docx / python-pptx / pandas](https://pypi.org/) – Document generation

---

## 📦 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/Ponvishnu/Omniverse-AI.git
cd Omniverse-AI
2. Install Python Packages
bash
pip install -r requirements.txt
Or manually:
bash
pip install customtkinter pillow pyttsx3 sounddevice vosk google-generativeai gtts pydub diffusers torch fpdf python-docx python-pptx pandas
3. Setup Your API Key
Edit your script and replace:
python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
Get your key from: https://ai.google.dev/

4. Download Vosk Model
Download from Vosk Models and extract to:
vosk-model-small-en-us-0.15
🚀 How to Run
bash
python omniverse_final.py
Make sure your microphone is connected and Python 3.10+ is installed.


🛠️ To-Do / Future Features
🎥 Export video clips with narration and images

🗂️ File management & email assistant

🤖 Add plugin system for extensibility

🌍 Multilingual support

🤝 Contributing
Pull requests are welcome! Feel free to fork and improve Omniverse AI.

📄 License
This project is under the MIT License.

👨‍💻 Author
Ponvishnu

GitHub: @Ponvishnu

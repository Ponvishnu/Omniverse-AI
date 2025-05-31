from image_ai import generate_image
from music_ai import sing_lyrics

def simulate_video_creation(prompt):
    generate_image(prompt, "scene.png")
    sing_lyrics("Narrating: " + prompt)
    print("🎬 Simulated video created with image and voice.")

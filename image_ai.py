from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="output.png"):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")  # Use "cuda" if you have a GPU
    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"✅ Image saved at {output_path}")

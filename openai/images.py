from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image
import gradio as gr


load_dotenv(find_dotenv())

client = OpenAI()


def generate_image(prompt):

    response = client.images.generate(
        model="gpt-image-1-mini",
        prompt=prompt.strip(),
        size="1024x1024",
        quality="high",
        output_format="png",
    )

    b64 = response.data[0].b64_json
    img_bytes = base64.b64decode(b64)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")

    return img


demo = gr.Interface(fn=generate_image, inputs="text", outputs=gr.Image())

demo.launch()

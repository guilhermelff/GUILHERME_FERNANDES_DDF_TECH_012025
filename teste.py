import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI
import base64
import apikey

client = OpenAI(
    api_key=apikey.key
)

def generate_image_url(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard"
    )
    return response.data[0].url

def plot_image(b64_image_data):
    image_data = base64.b64encode(b64_image_data)

    image = Image.open(io.BytesIO(image_data))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

url = generate_image_url("desenhe um gato")
print(url)

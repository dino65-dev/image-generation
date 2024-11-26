from huggingface_hub import InferenceClient
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
hf_token = os.getenv("hf_token")
client = InferenceClient(
    "stabilityai/stable-diffusion-3.5-large",
    token=hf_token
)

user_input = st.text_input("Enter your image prompt here")
st.title("Stable Diffusion 3.5 Large")
submit = st.button("Generate Image")
# output is a PIL.Image object
if submit:
    image = client.text_to_image(f"{user_input}")
    st.image(image, caption=f"{user_input}")

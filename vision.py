from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini model and get response
def get_gemini_response(input,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if(input!=""):
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# Set up Streamlit app

st.set_page_config(page_title="Gemini Vision Demo")

st.header("My Gemini Vision Application")
input = st.text_input("Input prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an Image..",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit = st.button("Tell me")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("Response is: ")
    st.write(response)
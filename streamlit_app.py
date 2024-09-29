import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDPPldAl-J3BkDeXkF4AUoJqm_ezwYwooA")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data": bytes_data
            }
            ]
        return image_parts
    else:
        raise FileNotFoundError("No File was uploaded")
st.set_page_config(page_title="WIE's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by IEEE WIE")
st.sidebar.write("Powered by Google Gemini")

st.header("RoboBill")
st.subheader("Made by IEEE WIE")
st.subheader("Manage your expenses with RoboBill")
input = st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("choose an image",type = ["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded Image",use_column_width=True)
ssubmit = st.button("Let's Go!")

input_prompt = """
You are an expert in reading invoices.We are going to upload an image of an iput and you will have to answer any type of questions that the user asks you.
you have to greet the ser first .Make sure to keep the fonts uniform and give the items list in a point-wise list format""" 

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data,input)
    st.write(response)

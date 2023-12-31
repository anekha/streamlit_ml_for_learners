
import streamlit as st
from PIL import Image
from io import BytesIO
import requests

st.set_page_config(page_title='About Us', page_icon="https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books_23-2149342941.jpg?w=2000", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title('About the team')

st.header(':blue[Deven Patten]')
st.text('I am a high school science teacher. I believe that coding improves your thinking ability and is meant to push you out of your comfort zone. That gets one to constantly reinvent oneself.')


st.header(':blue[Jeffrey Cheung]')
st.text('I am a data enthusiast, 35 years old, and Operations Manager in an IT company. I have a BSC in management and have been working mainly in the order to cash function. I like good food, sports and drinks. Understanding data has always helped me in decision making and in my career progression. I have been working mainly on excel, and I believe that the obvious next step is data science.')


st.header(':blue[Anekha Sokhal]')
st.text('After working as a data focused Energy Derivatives Trader for 7 years and subsequently working in global operations for a jewellery business, I wanted to bridge my experience in the data and business worlds by applying data science to making better business decisions. I studied MORSE (Maths, Operational Research, Statisics and Economics) at university and this recent 6 month course with Le Wagon has given me an invaluable deep dive into Data Science.')

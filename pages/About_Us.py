
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
st.text('I am interested in using data to make more efficient and effective business decisions. After studying Maths and Stats at uni and dabbling in programming over the years, I now want to commit to a longer course to have a full round Data Science learning experience')

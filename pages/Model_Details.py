import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import time
from PIL import Image
from io import BytesIO
import requests

st.set_page_config(page_title='Model Details', page_icon="https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books_23-2149342941.jpg?w=2000", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title('Gradient Boosting Classifier')

st.text('The final classification machine model used')

st.header('Pipeline')
image = Image.open('pages/pipeline_image.png')
#image = image.resize((300,400))
st.image(image)

st.header('Scoring Metrics')

d = {'Accuracy': 0.77, 'Precision': 0.76, 'Recall': 0.9, 'F1 Score': 0.82}

df = pd.DataFrame(data = d, columns = ['Accuracy','Precision', 'Recall','F1 Score'], index=[''])

st.table(df)

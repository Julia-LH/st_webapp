import streamlit as st
from PIL import Image
import urllib.request
import pandas as pd

# st.title('My first Streamlit app')
# st.write('''Welcome to my first web application!
#          This is a workspace to learn Streamlit. I'll be uploading stuff (images, dataframes, graphs), playing with the UI to explore all the possibilities and creating multipages. ''')


variables = pd.read_csv('variables_meteo_reduit.csv')
print(variables)

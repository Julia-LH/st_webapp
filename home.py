import streamlit as st
import os.path as path
from controllers.dob_management import home
from config.texts import title, intro

home(title=title, intro=intro)


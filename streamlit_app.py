# import streamlit as st

# print("Hello Roshni")
# st.title("💃🏼 Hello Streams 🎊")


import logging
import os

logging.basicConfig(level=logging.INFO)
logging.info("Hello Roshni")
logging.info(os.environ.get('RT_KEY)')


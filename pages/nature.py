from email.mime import image
import os
import streamlit as st
import streamlit as st
from matplotlib import image as img
import plotly.express as px

file_directory=os.path.dirname(os.path.abspath(__file__))

parent_directory=os.path.join(file_directory,os.pardir)

dir_of_interest=os.path.join(parent_directory,"resources")
IMAGE_PATH1= os.path.join(dir_of_interest, "images", "n1.jpg")
IMAGE_PATH2= os.path.join(dir_of_interest, "images", "n2.jpg")







st.title(":orange[**_Everything in nature invites us constantly to be what we are_**]:heartpulse:")
imag1=img.imread(IMAGE_PATH1)
imag2=img.imread(IMAGE_PATH2)

st.markdown(":red[_**If you love nature, you will find beauty anywhere._**]")

st.image([imag1,imag2],width=300)
st.markdown(":red[**_“No other sound can match the healing power of the sounds of nature.”_**]")

#displaying a video by simply passing a Youtube link
st.video("https://youtu.be/rOor-3U45tI")


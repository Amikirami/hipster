import streamlit as st
from streamlit_player import st_player
import cv2

st.title("Hipster V2.0")
decoded_objects=""

if st.button("Open Camera"):
    pic = st.camera_input("Take a picture")
    #pic = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    decoded_objects = detector.detectAndDecode(pic)
    #qr_data = [obj.data.decode('utf-8') for obj in decoded_objects]

st_player(decoded_objects)


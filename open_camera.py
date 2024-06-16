import cv2
import numpy as np
import streamlit as st
from streamlit_player import st_player
from streamlit.components.v1 import html
from PIL import Image

st.title("HIPSTER")
image = st.camera_input("Show QR code")
data = ""

if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

st.write(data)

for i in range(100):
    st.write("")
st_player(data, playing=True, play_inline=True)

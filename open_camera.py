import cv2
import numpy as np
import streamlit as st
from streamlit_player import st_player

st.title("HIPSTER")
image = st.camera_input("Show QR code")
data = ""


if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
else:
    st.write("Oops, I missed that! Could you please scan again? Thanks!")


for i in range(100):
    st.write("")
st_player(data, playing=True)

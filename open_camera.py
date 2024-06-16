import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
from streamlit_player import st_player
import cv2
from pyzbar.pyzbar import decode

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

st.title("Hipster V2.0")

if st.button("Open Camera"):
    pic = st.camera_input("Take a picture")
    #pic = cv2.imread(image_path)
    decoded_objects = decode(pic)
    qr_data = [obj.data.decode('utf-8') for obj in decoded_objects]

st_player(qr_data[0])


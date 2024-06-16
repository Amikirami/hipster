import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
from streamlit_player import st_player

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

st.title("Hitster V2.0")

if st.button("Open Camera"):
    st.camera_input("Take a picture")

st_player("https://www.youtube.com/watch?v=BY_XwvKogC8&list=RDBY_XwvKogC8&start_radio=1")


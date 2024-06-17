#import cv2
#import numpy as np
#import streamlit as st
#from streamlit_player import st_player
#
#st.title("HIPSTER")
#image = st.camera_input("Show QR code")
#data = ""
#
#
#if image is not None:
#    bytes_data = image.getvalue()
#    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#    detector = cv2.QRCodeDetector()
#    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
#else:
#    st.write("Oops, I missed that! Could you please scan again? Thanks!")
#st.write(data)
#
#for i in range(100):
#    st.write("")
#st_player(data, playing=True)

import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np


def play_spotify(song_url):
    # JavaScript to open link in new tab
    js = f"""
    <script type="text/javascript">
        var thisWindow = window;
        var popup = window.open("{song_url}", "_blank");
        popup.blur();
        thisWindow.focus();
    </script>
    """
    # Execute JavaScript in Streamlit app
    components.html(js, height=0, width=0)

# Streamlit app code
st.title('Play Spotify Song')
data=""
image = st.camera_input("Show QR code")
if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
    st.write(data)
    st.audio(data)
    st_player(data)

# Get user input (Spotify song URL)
song_url = st.text_input('Enter Spotify Song URL', value=data)

if st.button('Play Song'):
    if song_url:
        play_spotify(song_url)
        st.success(f"Playing song from {song_url}")
    else:
        st.warning("Please enter a Spotify song URL")



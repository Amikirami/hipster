import cv2
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def play_spotify(song_url):
    # JavaScript to open link in new tab
    js = """
    <script>
        var xPathRes = document.evaluate('/html/body/div/div/div/div[2]/div[4]/div[3]/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
        xPathRes.singleNodeValue.click();
    </script>
    """
    # Execute JavaScript in Streamlit app
    components.html(js)

image = st.camera_input("take a pic")

if image is not None:
    
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_GRAYSCALE)


    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
    

    if data!='':
        straight_qrcode = Image.fromarray(straight_qrcode)
        straight_qrcode = straight_qrcode.resize((256,256))
        st.image(straight_qrcode)
        st.write("# Found QR code")
        st.write(data)
        with st.expander("Show details"):
            st.write("BBox:", bbox)
            st.write("Straight QR code:", straight_qrcode)
        id = data.split('/')[-1]
        iframe_src = f"https://open.spotify.com/embed/track/{id}?utm_source=generator"
        components.iframe(iframe_src)

        # Get user input (Spotify song URL)
        song_url = st.text_input('Enter Spotify Song URL', value=data)
        
        if st.button('Play Song'):
            if song_url:
                play_spotify(song_url)
                st.success(f"Playing song from {song_url}")
            else:
                st.warning("Please enter a Spotify song URL")
        else:
            st.write("No QR code detected")

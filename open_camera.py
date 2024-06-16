import cv2
import numpy as np
import streamlit as st
from streamlit.components.v1 import html


st.title("HIPSTER")
image = st.camera_input("Show QR code")
data = ""

def open_page(url):
    open_script= """
        <script type="text/javascript">
            var a = document.createElement("a");
            a.href = '%s';
            var evt = document.createEvent("MouseEvents");
            //the tenth parameter of initMouseEvent sets ctrl key
            evt.initMouseEvent("click", true, true, window, 0, 0, 0, 0, 0,
                                        true, false, false, false, 0, null);
            a.dispatchEvent(evt);
        </script>
    """ % (url)

    print(open_script)
    html(open_script)


if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    st.write("Here!")
st.write(data)



st.button('PLAY', on_click=open_page, args=(data,))


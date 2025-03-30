import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import cv2

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Streamlit UI
st.title("Online Handwriting to Text Converter")
st.write("Upload a handwritten note image and extract text using OCR.")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to grayscale for better OCR results
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Perform OCR using EasyOCR
    extracted_text = reader.readtext(gray_image, detail=0, paragraph=True)
    extracted_text = " ".join(extracted_text)  # Ensure text is printed left to right

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("", extracted_text, height=250)

    # Provide download option
    if extracted_text:
        st.download_button("Download Extracted Text", extracted_text, file_name="extracted_text.txt")

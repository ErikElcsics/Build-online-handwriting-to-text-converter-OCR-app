# Build Online Handwriting to Text Converter (OCR) App

This Streamlit app converts handwritten notes into editable digital text using EasyOCR. It is useful for students, researchers, and professionals who want to digitize their handwritten content.

Features
- Upload handwritten note images (JPG, PNG, JPEG)
- Extract text using EasyOCR
- Display extracted text in an editable format
- Download extracted text as a .txt file

Installation:

Clone the repository
git clone https://github.com/ErikElcsics/Build-online-handwriting-to-text-converter-OCR-app.git
cd handwriting-ocr-app

Install dependencies
pip install streamlit easyocr pillow numpy opencv-python

Run the app
streamlit run online_handwriting_to_text_converter.py

Usage:
- Upload an image & extract text
- Upload an image containing handwritten text.
- Extracted text will be displayed in an editable text box.
- Download the text as a .txt file.

Notes
This app uses EasyOCR for handwriting recognition.

Ensure that the uploaded images are clear and well-lit for better accuracy.

![image](https://github.com/user-attachments/assets/1f39e34a-6da1-4a03-b25c-cdf7428b4bf3)

![image](https://github.com/user-attachments/assets/e4776c2f-87fb-4599-a51e-41836f7e5914)

Downloaded Extracted_text.txt

![image](https://github.com/user-attachments/assets/d655c6ad-f1b2-47e4-91db-b0700181c63a)

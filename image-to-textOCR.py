#pip install pytesseract

import pytesseract
from PIL import Image

# Load and preprocess the image
image = Image.open('venv/pexels-olena-bohovyk-3806690.jpg')
# Apply any necessary preprocessing steps

# Apply OCR to the image
text = pytesseract.image_to_string(image)

# Handle the extracted text
print(text)

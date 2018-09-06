from pytesseract import image_to_string 
from PIL import Image
from requests import get
from io import BytesIO

#Downloading Image from URL (SAMPLE)
response = get("http://13.127.3.3/wp-content/uploads/image-1.png") 

#Opening Image Object 
img = Image.open(BytesIO(response.content))

#OCR using Tesseract
text = image_to_string(img)

#Displaying Result
# Recognized Text must be in format = <NUM1><OPERATOR><NUM2>
if(text[1]=='+'): print(int(text[0])+int(text[2]))
if(text[1]=='-'): print(int(text[0])-int(text[2]))
if(text[1]=='*'): print(int(text[0])*int(text[2]))
if(text[1]=='/'): print(int(text[0])/int(text[2]))

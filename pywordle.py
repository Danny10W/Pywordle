import sys
from selenium import webdriver
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'..\\PywordleFiles\\tesseract\\tesseract.exe'
#import time

#activate virtual environment by running ".\venv\Scripts\Activate.ps1" in powershell
#need tesseract installed. I provide a install in the pyworle files folder
print(pytesseract.image_to_string('..\\PywordleFiles\\testimage6.png'))


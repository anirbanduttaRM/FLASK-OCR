# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:06:19 2019

@author: 138410
"""

from flask import Flask, jsonify
import sys
import pytesseract
from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np
#from StringIO import StringIO
#import Flask
app = Flask(__name__) 



@app.route('/process_image', methods=['POST'])
def process_image():
        image  = Image.open("screenshot.jpg")
        image.filter(ImageFilter.SHARPEN)
        new_size = tuple(2*x for x in image.size)
        image = image.resize(new_size, Image.ANTIALIAS)
        txt1 = pytesseract.image_to_string(image)
        #return jsonify({'Converted OCR A': str(txt1)})  
    
        image = cv2.imread("screenshot.jpg") 
        image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)
        cv2.threshold(cv2.bilateralFilter(image, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        txt2 = pytesseract.image_to_string(image)    
        return jsonify({'Converted OCR ': str(txt1)})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line argument
    except:
        port = 12345 # If you don't provide any port then the port will be set to 12345
        app.run(port=port, debug=True)
# Interactive GUI window to draw digits on canvas

from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np

model = load_model('mnist.h5')

def predict_digit(img):
    #resizing image to 28 x 28 pixels
    img = img.resize((28, 28))
    # convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    # reshaping to support model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

class App(tk.TK):
    def __init__(self):
        tk.TK.__init__(self)
        
        self.x = self.y = 0
        
    # Creating the elements
    self.canvas = tk.Canvas(self, width = 300, height = 300, bg = 'white', cursor = 'cross')
    self.label = tk.Label(self, text = 'Processing...', font=('Comic Sans', 48))
    self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting) 
    self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
    
    # Grid structure
    self.canvas.grid(row=0, column=0, pady=2, sticky=W)
    self.label.grid(row=0, column=1,pady=2, padx=2)
    self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
    self.button_clear.grid(row=1, column=0, pady=2)
    
    
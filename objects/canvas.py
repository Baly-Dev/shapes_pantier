import numpy as np
from PIL import Image
import os

class Canvas:
    """class responsible of creating the canvas"""
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def create(self, imagepath):
        canvas = Image.fromarray(self.data, 'RGB')
        
        os.chdir('drawings')
        canvas.save(imagepath)
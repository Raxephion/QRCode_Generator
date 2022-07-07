# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:10:56 2022

@author: Pierre-Henri Rossouw

60 Apps in 60 Days Challenge - App #8: QR Code generator




"""



import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 
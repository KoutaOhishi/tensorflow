#coding: utf-8
from PIL import Image
import os
import glob
# JPEG (512, 512) RGB
 
files = glob.glob('./train/*.jpg')
 
for f in files:
    img = Image.open(f)
    img_resize = img.resize((64, 64))
    ftitle, fext = os.path.splitext(f)
    print(ftitle,fext)
    img_resize.save(ftitle + fext)

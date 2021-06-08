
from PIL import Image, ImageFilter 

  

image = Image.open(r"c://Users/Patrick/Desktop/lab4_10679907.py") 

  
# Cropping the image  

cimage = image.crop((0, 0, 150, 150)) 

  
# Blurring the image that has been cropped

blurred_image = cimage.filter(ImageFilter.GaussianBlur) 

  
# Pasting the blurred image on the original image 

image.paste(blurred_image, (0,0)) 

  


image.save('blur.png')

#intended to implement this with a loop but that was a challenge

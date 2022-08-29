from PIL import Image
image_obj = Image.open("messi.jpg").convert('RGB').save('messi.jpeg')
rotated_image = image_obj.rotate(90)
rotated_image.save("messi_rotated.jpg")
rotated_image.image

error:
 Exception has occurred: AttributeError
'NoneType' object has no attribute 'rotate'
  File "/Users/ammaralsawai/Desktop/pil.py/main.py", line 3, in <module>
    rotated_image = image_obj.rotate(90) 

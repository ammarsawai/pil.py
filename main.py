from PIL import Image
image_obj = Image.open("messi.jpg").convert('RGB').save('messi.jpeg')
rotated_image = image_obj.rotate(90)
rotated_image.save("messi_rotated.jpg")
rotated_image.image


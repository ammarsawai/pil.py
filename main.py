from PIL import Image
image_obj = Image.open("abo.jpg").convert('RGB').save('new.jpeg')
rotated_image = image_obj.rotate(90)
rotated_image.save("abo_rotated.jpg")
rotated_image.image

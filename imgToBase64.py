import base64
from email.encoders import encode_base64
from os import listdir

print("Enter directory path to images.")

# val = input()
val = '/home/gold/Pictures/newFlag'
arr = listdir(val)
for f in arr:
    image = open(val.replace("'", "") + "/" + f, 'rb')
    image_read = image.read()
    image_encode = base64.b64encode(image_read)
    print(image_encode)

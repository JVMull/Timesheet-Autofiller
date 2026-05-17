from PIL import Image

img_name = input("Please enter image title:")
img = Image.open(img_name)
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged

rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")
# 33- 35 and 153-155

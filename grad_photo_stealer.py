from PIL import Image

img_name = "MagnifyRender.ashx"
alt_img_name = "MagnifyRender.jpeg"
# input("Please enter image title:")

TRANSPARENT_PIXELS = (0, 0, 0, 0)
# Open and convert to RGBA Image
try:
    img = Image.open(img_name)
except:
     print("Different name")
     img = Image.open(alt_img_name)
else:
     print("Image Processed")

rgba = img.convert("RGBA")


with rgba as im:
    px = im.load()
    # top bar = x: 33 - 155 y: 33-35
    for x in range(32, 156 + 1):
        for y in range(32, 36 + 1):
            px[x, y] = TRANSPARENT_PIXELS
    # left bar = x: 33 - 35 y: 36 - 155
    for x in range(32, 36 + 1):
            for y in range(35, 156 + 1):
                px[x, y] = TRANSPARENT_PIXELS
    # right bar = x: 153 - 155 y: 36 - 155   
    for x in range(152, 156 + 1):
            for y in range(35, 156 + 1):
                px[x, y] = TRANSPARENT_PIXELS
    # bottom bar = x: 36 - 152 y: 153 - 155
    for x in range(35, 153 + 1):
            for y in range(152, 156 + 1):
                px[x, y] = TRANSPARENT_PIXELS
im.save('output.png')



#  class PixelAccess

#     __getitem__(self, xy: tuple[int, int]) → float | tuple[int, ...]

#         Returns the pixel at x,y. The pixel is returned as a single value for single band images or a tuple for multi-band images.

#         Parameters:

#             xy – The pixel coordinate, given as (x, y).
#         Returns:

#             a pixel value for single band images, a tuple of pixel values for multiband images.

#     __setitem__(self, xy: tuple[int, int], color: float | tuple[int, ...]) → None

#         Modifies the pixel at x,y. The color is given as a single numerical value for single band images, and a tuple for multi-band images. See Colors for more information.

#         Parameters:

#                 xy – The pixel coordinate, given as (x, y).

#                 color – The pixel value according to its mode, e.g. tuple (r, g, b) for RGB mode.


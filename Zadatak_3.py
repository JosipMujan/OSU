import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
plt.subplot(2,3,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

#a) Lighten the image
bright = img + 50
bright = np.clip(bright, 0, 255)
plt.subplot(2,3,2)
plt.imshow(bright.astype(np.uint8))
plt.title("Brightened image")
plt.axis("off")

#b)Second quarter of the image by width
h, w, canals = img.shape                # h,w = img.shape[:2]
img_quarter = img[:, w//4:w//2]
plt.subplot(2,3,3)
plt.imshow(img_quarter)
plt.title("Second Quarter of the image by width")
plt.axis("off")

#c) Rotate the image by 90 degrees CW
rot = np.rot90(img, -1)
plt.subplot(2,3,4)
plt.imshow(rot)
plt.title("Rotated image")
plt.axis("off")

#d) Mirror image horizontally
mirror = np.fliplr(img)
plt.subplot(2,3,5)
plt.imshow(mirror)
plt.title("Mirrored image")
plt.axis("off")

plt.show()
import matplotlib.pyplot as plt
import lib

img = lib.load_img("smol.png")

plt.imshow(img)
plt.show()

(x, y) = (0, 0)

pxls = img.load()

matrix = []
list = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        rgb = pxls[x, y]
        hex = lib.rgb2int(rgb)

        list.append(hex)

    matrix.append(list)
    list = []

lib.box_blur(matrix)

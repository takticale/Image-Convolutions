
from PIL import Image

# ===== BASIC ===== #


def decode(color):
    color = color.split(';')[:3]

    return color


def grayscale(image):
    img = Image.open(image).convert("LA")

    return img


def load_img(image):
    img = Image.open(image)

    return img
	
	
def rgb2int(color):
    string = ''
    for value in color:
        _ = str(value) + ";"
        string += _
    return string


# ===== KERNELS ===== #

def box_blur(matrix):
    width = len(matrix)
    height = len(matrix[0])

    for i in range(width):
        for j in range(height):
            if i - 1 >= 0 and j - 1 >= 0 and i + 1 <= width - 1 and j + 1 <= height - 1:
                print(i, j)

                leftup = decode(matrix[i - 1][j - 1])
                rightup = decode(matrix[i + 1][j - 1])
                leftdown = decode(matrix[i - 1][j + 1])
                rightdown = decode(matrix[i + 1][j + 1])

                centerdown = decode(matrix[i][j + 1])
                centerup = decode(matrix[i][j - 1])
                centerright = decode(matrix[i + 1][j])
                centerleft = decode(matrix[i - 1][j])

                center = decode(matrix[i - 1][j - 1])
                print("\n\n")

            else:
                print("kernel inapplicable")
                continue

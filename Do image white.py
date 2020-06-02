from PIL import Image

img = Image.open('data\\Sprites\\next.png')
data = img.load()
x, y = img.size

for i in range(x):
    for j in range(y):
        data[i, j] = (255 - data[i, j][0], 255 - data[i, j][1], 255 - data[i, j][2])

img.save("data\\Sprites\\next.png")
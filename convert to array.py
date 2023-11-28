from PIL import Image
import numpy as np
from matplotlib import cm


image = Image.open("output_0016.png")
row,col =  image.size
data = []
pixels = image.load()
for i in range(row):
    for j in range(col):
        r,g,b =  pixels[i,j]
        data.append(r)
print(data[:10])

a = np.asarray(image)

print(a[:5,:5])
b = np.array(a, copy=True)  
for i in a:
    for j in i:
        print(np.mean(a[i,j]))
np.savetxt('myarray.txt', a)
data = np.array(data)

new_image = Image.fromarray(data)   
im = Image.fromarray(np.uint8(cm.gist_earth(data)*255))
new_image.save('00000.png')
im.save('00001.png')
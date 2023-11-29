from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def image_process(fp):
    image = Image.open(f"{fp}.png")
    col,row =  image.size
    print(row,col)
    data = []
    pixels = image.load()
    for i in range(row):
        # temp = []
        for j in range(col):
            r,g,b =  pixels[j,i]
            data+=[r,g,b]
        # data.append(temp)
    return data

# print(image_process(1))
    # 
# print(data[:10])
# image.show()
# plt.imshow(image)
# with open("output.txt", "w") as txt_file:
#     for line in data:
#         txt_file.write(f" {line}") # works with any number of elements in a line

# array = np.array(data, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
def save_img(arr):
    # arr = np.array(arr, dtype=np.uint8)
    new_image = Image.fromarray(arr)
    new_image.save('new.png')

print('works')
def _format(arr):
    res = np.zeros([1080,1920,3], dtype=np.uint8)
    array = np.zeros([1080,5760], dtype=np.uint8)
    print(len(res))
    n = len(arr)//5760
    m = len(arr)%5760
    
    for i in range(n):
        for j in range(5760):
            array[i,j] = arr[i*5760+j]
    for j in range(m):
        array[n,j] = arr[n*5760+j]
        
    for i in range(1080):
        for j in range(1920):
            # print(i, j*3)
            res[i,j] = [array[i,j*3], array[i,j*3+1], array[i,j*3+2]]
    # for i in range(n):
    #     for j in range(1920):
    #         res[i,j] = [arr[i*5760+j*3], arr[i*5760+j*3+1], arr[i*5760+j*3+2]]
    # for j in range(m//3):
    #     res[n,j] = [arr[n*5760+j*3], arr[n*5760+j*3+1], arr[n*5760+j*3+2]]
    # for j in range(m%3):
        
    # todo
    return res






def convert(fp,ft):    
    arr = []
    content = ""
    for i in range(1,2):
        # f = open(f'{fp}{i}.{ft}', 'rb')
        f = open(fp, 'rb')

        # content = f.read()
        for a in f:
            for b in a:
                arr.append(b)
        # print(arr)
    # print(arr, len(arr))
    # _write(arr,tt)
    return arr

def _write(arr, tt):
    f = open(f'output.{tt}', 'wb') 
    # for a in arr:
    #     f.write(chr(a))
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            i = j
    f.write(bytearray(arr[:i+1]))
    f.close()

save_img(_format(convert(input('filename to convert: '),input('file type to convert: '))))
#generated new.png
data = image_process('new')
_write(data,input('output type: '))
# convert('a','pdf','pdf')
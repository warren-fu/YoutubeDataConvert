from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os, shutil
import cv2
import skvideo.io

WIDTH = 1920
HEIGHT = WIDTH//16 * 9

def image_process(fp):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f"../images/{fp}.png")
    image = Image.open(file_path)
    
    col, row = image.size
    print(row, col)
    data = []
    pixels = image.load()
    
    for i in range(row):
        for j in range(col):
            r, g, b = pixels[j, i]
            data.extend([r, g, b])
    
    return data
def vid_process(fp,n):
    data = []
    for i in range(n):
        data += image_process(f'{fp}{n}')
    return data

# Use PIL to create an image from the new array of pixels
def save_img(arr,n):
    # arr = np.array(arr, dtype=np.uint8)
    new_image = Image.fromarray(arr)
    new_image.save(f'./images/output{n}.png')

# print('works')
def format_full(arr):
    res = np.zeros([HEIGHT,WIDTH,3], dtype=np.uint8)
    
    for i in range(HEIGHT):
        w2 = i*WIDTH*3
        for j in range(WIDTH):
            k = j*3
            # print(i, j*3)
            res[i,j] = [arr[w2 + k], arr[w2 + k + 1], arr[w2 + k + 2]]
    return res


def format_(arr):
    res = np.zeros([HEIGHT,WIDTH,3], dtype=np.uint8)
    array = np.zeros([HEIGHT,WIDTH*3], dtype=np.uint8)
    w2 = WIDTH*3
    n = len(arr)//w2
    m = len(arr)%w2
    
    for i in range(n):
        for j in range(w2):
            array[i,j] = arr[i*w2+j]
    for j in range(m):
        array[n,j] = arr[n*w2+j]
        
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # print(i, j*3)
            res[i,j] = [array[i,j*3], array[i,j*3+1], array[i,j*3+2]]
            
    return res

def convert(fp, ft):
    arr = []
    # Adjust the path to be relative to the script's location
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f'../tests/{fp}.{ft}')
    with open(file_path, 'rb') as f:
        for a in f:
            for b in a:
                arr.append(b)
    return arr

def _write(arr, ft):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path,f'../output/output.{ft}')
    f = open(file_path, 'wb') 
    # for a in arr:
    #     f.write(chr(a))
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            i = j
    f.write(bytearray(arr[:i+1]))
    f.close()

# save_img(_format(convert(input('filename to convert: '),input('file type to convert: '))))
# #generated new.png
# data = image_process('new')
# _write(data,input('output type: '))
# convert('a','pdf','pdf')
def clear():
    folder = './images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return 0
    return 1

def to_vid():
    outputfile = '../tests/output.mp4'  #our output filename
    writer = skvideo.io.FFmpegWriter(outputfile, outputdict={
    '-vcodec': 'libx264',  #use the h.264 codec
    '-crf': '0',           #set the constant rate factor to 0, which is lossless
    '-preset':'veryslow'   #the slower the better compression, in princple, try 
                            #other options see https://trac.ffmpeg.org/wiki/Encode/H.264
    }) 
    images = []
    for f in os.listdir('./images'):
        if f.endswith('png'):
            images.append(f)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    # out = cv2.VideoWriter(outputfile, fourcc, 5, (WIDTH, HEIGHT))
    # fourcc = cv2.cv.CV_FOURCC(*'XVID')
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('../tests/output.avi',fourcc, 20.0, (WIDTH,HEIGHT))
    
    # frame = cv2.imread(f'./blank.png')
    # out.write(frame) # Write out frame to video
    for image in images:
        frame = cv2.imread(f'./images/{image}')


        writer.writeFrame(frame[:,:,::-1])  #write the frame as RGB not BGR
        ret=cv2.waitKey(10)
        if ret==27: #esc
            break



        # out.write(frame) # Write out frame to video

        # cv2.imshow('video',frame)
        # if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        #     break
        
    # out.release()
    # cv2.destroyAllWindows()
    
    
def break_vid(vid_name):
    cam = cv2.VideoCapture(f"../tests/{vid_name}") 
    try:
        if not os.path.exists('../src/data'): 
            os.makedirs('../src/data') 
    
    # if not created then raise error 
    except OSError:     
        print ('Error: Creating directory of data') 
    currentframe = -1
    while(True): 
        
        # reading from frame 
        ret,frame = cam.read() 
    
        if ret: 
            if currentframe == -1:
                currentframe = 0
                continue
            # if video is still left continue creating images 
            name = f'./data/output{currentframe}.png'
            print ('Creating...' + name) 
    
            # writing the extracted images 
            cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        else: 
            cam.release() 
            return currentframe
    
def main():
    while(1):
        a = input('Enter A (data to video) or B (video to data): ')
        if a == "A":
            clear()
            fp = str(input('Enter the File Name: '))
            ft = str(input('Enter the File Type: '))
            data = convert(fp,ft)
            n = len(data)
            
            t = WIDTH*HEIGHT*3
            full = n//(t)
            empty = n%(t)
            
            for i in range(full): save_img(format_full(data[i*t:i*t+t]),i)
            save_img(format_(data[full*t:]),full)
            print(f'length is {full+1}')
            
            # to_vid()
            
        elif(a == "B"):
            n = (int)(input('Enter the number of photos'))
            # n = break_vid(input('Enter the video name: '))
            print(n)
            output = input('Enter the Output File Type')
            data = []
            for i in range(n): data += image_process(f'output{i}')
            _write(data,output)
        else:
            break
main()
from PIL import Image
import numpy as np
import os, shutil, sys
import cv2

WIDTH = 7680
HEIGHT = 4320
SCALE = 5
FPS = 48

def clear_directory():
    base_path = os.path.dirname(__file__)
    folder_path = os.path.join(base_path, f'data')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return -1
    return 0

def convert_video_to_frames(path):
    video = cv2.VideoCapture(path)
    count = 0
    success = 1
    base_path = os.path.dirname(__file__)
    while success:
        success, image = video.read()
        print(count)
        try:
            cv2.imwrite(os.path.join(base_path, f'data/frame{count}.png'), image)
        except Exception as e:
            print(e)
            return count
        count += 1
    return count-1

def image_process(filename):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f"data/{filename}")
    image = Image.open(file_path)
    data = []
    pixels = image.load()

    for i in range(2,HEIGHT,SCALE):
        for j in range(2,WIDTH,SCALE):
            r, g, b = pixels[j, i]
            data.extend([r, g, b])
    return data

def bytes_to_file(arr, filename):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path,f'../../{filename}')
    f = open(file_path, 'wb')
    last_index = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            last_index = j
    f.write(bytearray(arr[:last_index+1]))
    f.close()

def generator():
    if len(sys.argv) < 2:
        print("Pass in filename")
        exit(-1)
    if len(sys.argv) > 2:
        print("Too many arguments")
        exit(-1)
    clear_directory()
    filename = str(sys.argv[1])
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f'../../{filename}')
    number_of_frames = convert_video_to_frames(file_path)

    data = []
    print(f"number of frames: {number_of_frames}")
    for i in range(number_of_frames):
        data += image_process(f'frame{i}.png')
    bytes_to_file(data, f"{".".join(filename.split('.')[:-1])}")
    # clear_directory() # uncomment when debugging
    exit(0)

if __name__ == "__main__":
    generator()

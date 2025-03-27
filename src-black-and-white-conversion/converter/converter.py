from PIL import Image
import numpy as np
import os, shutil, sys
import cv2

WIDTH = 7680
HEIGHT = 4320
SCALE = 5
FPS = 48

"""
In youtube, there's a different bitrate limit for each resolution so I went ahead and found the max bitates for each 
resolution. 

Recommended bit-rate for 7680x4320 @ 48,50,60fps: 120-240 Mbps or 120,000,000 - 240,000,000 bytes/second
As of right now, if we encode every pixel with 3 bytes of data, we get 7680*4320*48*3 = 4,777,574,400 bytes/second
Now, to get it within a safe range of the bit-rates, we can make each "pixel" of data 5x5 pixels, resulting in a new
bit-rate of 4,777,574,400/5^2 = 191,102,976 bytes/second or 191.102.976 Mbps. This now fits comfortable within the 
recommended bit-rate for 7680x4320 @ 48fps.

In theory, this works very well but in practice, even separating a video into individual frames still results in data 
loss through image compression. This version of the program will continue to attempt to convert everything into fully
colored frames to utilize as much of the bit-rate as possible. There will be another version which will only utilize
black and white pixels.
"""

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

def convert_to_byte_array(filename):
    byte_array = []
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f'../../tests/{filename}')
    with open(file_path, 'rb') as f:
        for line in f:
            for byte in line:
                byte_array.append(byte)
    return byte_array

def to_vid(output_filename):
    base_path = os.path.dirname(__file__)
    output_file = os.path.join(base_path, f'../../{output_filename}')
    # Create a VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec for the output video file
    video = cv2.VideoWriter(output_file, fourcc, FPS, (WIDTH, HEIGHT))
    images = []
    folder_path = os.path.join(base_path, f'data')
    for f in os.listdir(folder_path):
        if f.endswith('png'):
            images.append(f)

    for image in images:
        frame = cv2.imread(os.path.join(base_path, f'data/{image}'))
        video.write(frame[:, :, ::-1])  # write the frame as RGB not BGR

    video.release()
    cv2.destroyAllWindows()

# Use PIL to create an image from the new array of pixels
def save_img(arr, n):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, f'data/output{n}.png')
    new_image = Image.fromarray(arr)
    new_image.save(file_path, 'PNG')

def format_frame(arr):
    res = np.zeros([HEIGHT, WIDTH, 3], dtype=np.uint8)
    byte_index = 0
    arr += [0]*(HEIGHT*WIDTH*3//(SCALE**2)-len(arr))
    for i in range(0,HEIGHT,SCALE):
        for j in range(0,WIDTH,SCALE):
            temp = arr[byte_index:byte_index+3]
            for x in range(i,i+SCALE):
                for y in range(j,j+SCALE):
                    res[x, y] = temp
            byte_index += 3
    return res

def converter():
    if len(sys.argv) == 1:
        print("Pass in filename")
        exit(-1)
    if len(sys.argv) > 2:
        print("Too many arguments")
        exit(-1)
    clear_directory()
    filename = str(sys.argv[1])
    # TODO (warren-fu) Add support for chunking to avoid excessive RAM usage
    data = convert_to_byte_array(filename)

    n = len(data)
    bytes_per_frame = WIDTH * HEIGHT * 3 // (SCALE**2)
    num_full_frames = n // bytes_per_frame

    for i in range(num_full_frames):
        save_img(
            format_frame(data[num_full_frames*bytes_per_frame:(num_full_frames+1)*bytes_per_frame]),
            i
        )
        print(f"low: {num_full_frames*bytes_per_frame}, high: {(num_full_frames+1)*bytes_per_frame}")
    save_img(
        format_frame(data[num_full_frames * bytes_per_frame:]),
        num_full_frames
    )
    print("Completed conversion")
    to_vid(f'{filename}.mp4')
    #clear_directory() #Uncomment for debugging
    exit(0)

if __name__ == "__main__":
  converter()

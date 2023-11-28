import numpy as np
def convert(fp,ft,tt):    
    arr = []
    for i in range(1,2):
        with open(f'{fp}{i}.{ft}', 'rb') as f:
            for x in f:
                for a in x:
                    arr.append(a)
    # print(arr, len(arr))
    _write(arr,tt)

def _write(arr, tt):
    f = open(f'output.{tt}', 'w+') 
    for a in arr:
        f.write(chr(a))
    f.close()
    
convert('text','txt','cpp')
# main(input('file name: '), input('file type: '), input('target file type: '))
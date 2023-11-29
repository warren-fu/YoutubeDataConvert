import numpy as np
# import binascii as 

def convert(fp,ft,tt):    
    arr = []
    content = ""
    for i in range(1,2):
        # f = open(f'{fp}{i}.{ft}', 'rb')
        f = open(fp, 'rb')
        # content = f.read()
        for a in f:
            for b in a:
                arr.append(b)
        print(arr)
    # print(arr, len(arr))
    _write(arr,tt)

def _write(arr, tt):
    f = open(f'output.{tt}', 'wb') 
    # for a in arr:
    #     f.write(chr(a))
    f.write(bytearray(arr))
    f.close()
    
convert('a','pdf','pdf')
# main(input('file name: '), input('file type: '), input('target file type: '))
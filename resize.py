import os
from PIL import Image as PILImage

dirfrom=''    #directory of source files
dirto=''    #directory of resized files

directory = os.listdir('./'+dirfrom)

for file in directory:
    try:
        with PILImage.open('./'+dirfrom+'/'+file) as im:
        transed=im.resize((96,96))#원본을 300 by 300 변경
        transed.save('./'+dirto+'/'+'resized'+file)
    except:
        print("cannot resize file")
from os import listdir,path,makedirs
import os
from os.path import isfile, join
from wand.image import Image
input_path = r'D:\www\pdf-image-convert\input'
output_path ='D://www//pdf-image-convert//output_folder//'
outputFileExtentino = "webp"

for file in listdir(input_path):
    if isfile(join(input_path, file)) and file.endswith('.pdf'):
        file_path = join(input_path, file)
        print(file_path)
        folder_path= output_path+file.split(".pdf")[0]+"//"
        i=1
        page = 1
        if not path.exists(folder_path):
            makedirs(folder_path)
        with Image(filename = file_path, resolution = 200) as pdfimage:
            for img in pdfimage.sequence:
                if i in []:
                    i+=1
                    continue
                if i in []:
                    page += 2
                if i >= 1:
                    image = Image(image = img)
                    image.save(filename = folder_path + str(page) + "." + outputFileExtentino)
                    page += 1
                i += 1
    print('complete')
    
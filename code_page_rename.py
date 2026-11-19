from os import listdir,path,makedirs
from os.path import join, exists
import shutil
input_path = 'F://pdf//output_folder//input//'
output_path ='F://pdf//output_folder//new//'
outputFileExtentino = "webp"
# initialPageNo = 1
# pageLimit = 506
# finalPageNo = initialPageNo + pageLimit

index = 1
for page in range(20, 613):
    input_file_path = join(input_path, str(page)+'.webp')
    print(input_file_path)
    if exists(input_file_path):
        out_file_path = output_path + str(index)+'.webp'
        shutil.copy(input_file_path, out_file_path)
        index +=1
    page += 1
print('ok')

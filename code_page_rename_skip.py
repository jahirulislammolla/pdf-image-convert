from os import listdir,path,makedirs
from os.path import join, exists
import shutil
input_path = 'F://pdf//output_folder//input//'
output_path ='F://pdf//output_folder//new2//'
outputFileExtentino = "webp"
# initialPageNo = 1
# pageLimit = 506
# finalPageNo = initialPageNo + pageLimit

index = 1
for page in range(1, 1100):
    input_file_path = join(input_path, str(page)+'.webp')
    # print(input_file_path)
    if exists(input_file_path):
        out_file_path = output_path + str(index)+'.webp'
        shutil.copy(input_file_path, out_file_path)
        index +=1
        while index in [12,30,48,49,50,78,110,111,112,134,142,169,170,182,270,182,282,292,303,304,382,402,436,437,438,448,489,490,502,550,551,552,567,568,586,612,624,625,626,638,652,674,683,684,696,710,776,785,786,840,841,842,900,913,914,928,954,990,1010,1026,1060,1071,1072]:
            index += 1
            print(page, index)
    page += 1
print('complete')

import exifread
import os

import tmgshare

path_name = "z:\\photosmaster\\IMG_1941.JPG"


def make_file_by_date_subdir(path_name):
    f = path_name.split('\\')
    filename = f[len(f)-1]

    f = open(path_name, 'rb')
    tags = exifread.process_file(f, details=False)

    rawdate= str(tags["Image DateTime"])
    d = rawdate.split(' ')
    year_month_day = d[0].split(':')

    
    date_directory = str.format("{0}\\{1}\\{2}", year_month_day[0], year_month_day[1], year_month_day[2])
    if not os.path.exists(date_directory):
        os.makedirs(date_directory)

    return date_directory +"\\" + filename
    

print(make_file_by_date_subdir(path_name))
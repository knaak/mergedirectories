import exifread
import os
from os import listdir

import time, sys

import tmgshare

import pytz
import datetime
from win32com.propsys import propsys, pscon

source_dir = "Z:\\PhotosMaster"

def getmediacreationtime(path_name):
    properties = propsys.SHGetPropertyStoreFromParsingName(path_name)
    dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
    if (not dt): return ""
    return [dt.year, dt.month]
    

def make_file_by_date_subdir(path_name):
    f = path_name.split('\\')
    filename = f[len(f)-1]

    try:
        f = open(path_name, 'rb')
        tags = exifread.process_file(f, details=False)
        f.close()

        if (tags):
            rawdate= str(tags["Image DateTime"])
            d = rawdate.split(' ')
            year_month_day = d[0].split(':')
        else:
            year_month_day = getmediacreationtime(path_name)
            if (type(year_month_day) == None):
                return ""
            if (len(year_month_day) != 2):
                return ""
        
        date_directory = str.format("{0}\\{1}\\{2:02d}", source_dir, year_month_day[0], int(year_month_day[1]))
        if not os.path.exists(date_directory):
            os.makedirs(date_directory)

        return date_directory +"\\" + filename
    except:
        return ""    
    

with os.scandir(source_dir) as entries:
    for file in entries:
        if (not file.is_file()): continue

        src_file = file.path
        dest_file = make_file_by_date_subdir(file.path)
        
        if (not dest_file):
            print("file does not have exif:", src_file)
            continue

        dest_filepath = os.path.join(source_dir, dest_file)
        try:
            os.rename(src_file, dest_filepath)
            print(str.format("Moved {0} to {1}", src_file, dest_filepath))
        except:
            print("error moving ", src_file)

        sys.stdout.flush()

  



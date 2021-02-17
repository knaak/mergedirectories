import exifread
import os
from os import listdir

import time, sys

import tmgshare

import pytz
import datetime
from win32com.propsys import propsys, pscon

source_dir = "Z:\\PhotosMaster"

if (len(sys.argv) == 2):
    source_dir = sys.argv[1]
    
print("Using directory:", source_dir)
input("Press enter to start the process")

with os.scandir(source_dir) as entries:
    for file in entries:
        if (not file.is_file()): continue

        src_file = file.path
        dest_file = tmgshare.make_file_by_date_subdir(file.path)
        
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

  



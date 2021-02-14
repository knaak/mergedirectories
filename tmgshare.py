import os
import hashlib
import time, sys

from shutil import copyfile

def file_md(filename):    
    with open(filename, 'rb') as file_to_check:
        data = file_to_check.read()    
        return hashlib.md5(data).hexdigest()

def combine_file(dir, file, ext):
    return str.format("{0}\\{1}.{2}", dir, file, ext)

def create_unique_name(destination_dir, filepart, fileext):
    while (os.path.exists(combine_file(destination_dir, filepart, fileext))):
        filepart = filepart +"_"

    return combine_file(destination_dir, filepart, fileext)

def copyfile_unique(fullpath, destinationdir):
    fileparts = fullpath.split('\\')
    filename = fileparts[len(fileparts)-1]
    filename_parts = filename.split('.')
    filename_ext = filename_parts[len(filename_parts)-1]
    filename_parts.pop()
    filename_wo_ext = ''.join(filename_parts)

    destination_file = str.format("{0}\\{1}.{2}", destinationdir, filename_wo_ext, filename_ext)

    new_name =""
    #first lets make sure that the name doesn't collide
    if (os.path.exists(destination_file)):
        src_md5 = file_md(fullpath)
        dest_md5 =  file_md(destination_file)

        if (src_md5 == dest_md5): 
            print("File exists in destination", fullpath)
    else:
        new_name = create_unique_name(destinationdir, filename_wo_ext, filename_ext)
        copyfile(fullpath, new_name)
        print(str.format('Copied {0} as {1} ', fullpath, new_name))

    return new_name

def make_file_by_date_subdir(path_name):
    f = path_name.split('\\')
    filename = f[len(f)-1]

    f = open(path_name, 'rb')
    tags = exifread.process_file(f, details=False)

    rawdate= str(tags["Image DateTime"])
    d = rawdate.split(' ')
    year_month_day = d[0].split(':')

    
    date_directory = str.format("{0}\\{1}\\{2}", year_month_day[0], year_month_day[1], year_month_day[2])
    os.makedirs(date_directory)

    return date_directory +"\\" + filename

def create_list_of_unique_files(source_dir):
    count_of_found_files = 0
    count_duplicates = 0
    dict_hashes = dict()
    print ("This will create a dictionary by hash of file contents with all of the locations of duplicates")
    for root, subdirs, files in os.walk(source_dir):
        for file in files:        
            if (file.endswith('.del')): continue

            filePath = os.path.join(root, file)
            md5 = file_md(filePath)
            sys.stdout.flush()

            if (md5 in dict_hashes):
                dict_hashes[md5] = dict_hashes[md5] + "," + filePath
                count_duplicates = count_duplicates +1
                print('d',end='')
            else:
                count_of_found_files = count_of_found_files +1
                dict_hashes[md5] = filePath
                print(".", end='')

    print(str.format("Found {0} files of which {1} were actually duplicates", count_of_found_files, count_duplicates))
    return dict_hashes

def go_copy_files(dict_hashes, source_dir, destination_dir):
    count = 0
    for item in dict_hashes:
        locations = dict_hashes[item].split(',')
        new_name = copyfile_unique(locations[0], destination_dir)
        count= count+1
        sys.stdout.flush()

        if (new_name):
            print(str.format("Copied {0} to new location as {1}", item, new_name))

        if ((count % 250) == 0):
            print("Percent complete:", int((count/len(dict_hashes)*100)))

def go_delete_duplicate(dict_hashes, directory):
    count = 0
    for item in dict_hashes:
        locations = dict_hashes[item].split(',')
        if (len(locations) == 1): 
            continue

        #I want to keep the original with the shortest name, just because
        ndx = 0
        ndx_len = 1000
        count = 0
        for files in locations:            
            if (len(files) < ndx_len):
                ndx_len = len(files)
                ndx = count
            count = count +1

        # now I have the ndx of the shortest len, rename the others
        c = 0
        for files in locations:
            if (c == ndx): 
                print("Keep:", files)                
            else:
                if (".del" not in files): 
                    print("Delete:", files)                
                    os.rename(files, files+".del")
            c= c+1
            print("=================================================================")
            sys.stdout.buffer.flush()

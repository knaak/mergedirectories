import os
import hashlib

from shutil import copyfile

source_dir = "Z:\\amazon-backup\\MyPhotos"
desintation_dir = "Z:\\PhotosMaster"

count_of_found_files = 0
count_duplicates = 0
count_of_files_copied = 0
count_of_files_duplicate_name_different_contents = 0


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

    
    
dict_hashes = dict()

print ("This will create a dictionary by hash of file contents with all of the locations of duplicates")
for root, subdirs, files in os.walk(source_dir):
    for file in files:        
        filePath = os.path.join(root, file)
        md5 = file_md(filePath)
        if (md5 in dict_hashes):
            dict_hashes[md5] = dict_hashes[md5] + "," + filePath
            count_duplicates = count_duplicates +1
            print('d',end='')
        else:
            count_of_found_files = count_of_found_files +1
            dict_hashes[md5] = filePath
            print(".", end='')

print(str.format("Found {0} files of which {1} were actually duplicates", count_of_found_files, count_duplicates))

#input("press enter to start copy process")

print("Now we will move exactly one copy of each of the duplicates to its new location, ignoring original directory structure")

for item in dict_hashes:
    locations = dict_hashes[item].split(',')
    #print(str.format("This file {0} was found in {1} locations", item, len(dict_hashes[item].split(','))))
    new_name = copyfile_unique(locations[0], desintation_dir)
    if (new_name):
        print(str.format("Copied {0} to new location as {1}", item, new_name))
    
print("done, merged directory should have exactly 1 copy of every file with any name collisions with different contents resolved by appending a _")

print(str.format("Found {0} files, of which {1} were duplicates, which resulted in {2} collisions in merged folder and {3} files actually copied", count_of_found_files, count_duplicates, count_of_files_duplicate_name_different_contents, count_of_files_copied))
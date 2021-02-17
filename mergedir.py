import tmgshare as tmg
import sys

source_dirs = ["Z:\\amazon-backup\\MyPhotos", "Z:\\amazon-backup\\photosrestore", "Y:\\backups\\MyPhotos", "Z:\\backups\\MyPhotos", "Z:\\backups\\backups\\oldrives\\MyPhotos", "Z:\\backups\\backups\\oldrives\\Likely Duplications", "Y:\\backups\\backups\\oldrives\\MyPhotos", "Y:\\backups\\Pictures"]
destination_dir = "Z:\\PhotosMaster.2"

if (len(sys.argv)==3):
    source_dirs = [ sys.argv[1] ]
    destination_dir = sys.argv[2]

input(str.format("Press Enter to start merging {} to {}", str(source_dirs),destination_dir))

for source_dir in source_dirs:
    print("processing ", source_dir)
    dict_hashes = tmg.create_list_of_unique_files(source_dir)
    tmg.go_copy_files(dict_hashes, source_dir, destination_dir)

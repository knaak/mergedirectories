import tmgshare as tmg

source_dirs = ["Z:\\amazon-backup\\MyPhotos\\2000"]#,"Z:\\amazon-backup\\MyPhotos", "Z:\\amazon-backup\\photosrestore", "Y:\\backups\\MyPhotos", "Z:\\backups\\MyPhotos", "Z:\\backups\\backups\\oldrives\\MyPhotos", "Z:\\backups\\backups\\oldrives\\Likely Duplications", "Y:\\backups\\backups\\oldrives\\MyPhotos", "Y:\\backups\\Pictures"]
destination_dir = "Z:\\PhotosMaster"

for source_dir in source_dirs:
    dict_hashes = tmg.create_list_of_unique_files(source_dir)
    tmg.go_copy_files(dict_hashes, source_dir, destination_dir)

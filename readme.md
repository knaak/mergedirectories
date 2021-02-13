Designed to take my many Photo's back ups located in several places on my computers, old hard drives, DVD backups
and be able to merge them into a single Master folder which is virtually guarenteed to not have duplicate photos. 

Program works in two steps to allow for review before changes are made:

Step 1.
    Create a dictionary of MD5 hashes of the file contents of a directory (and all subdirs)
    For every md5, i have a list of files that are actually duplicates somewhere else in the that structure


Now i have a KV of every file in that directory, where K=Hash V=Comma Separated list of physical locations.

Step 2.
    I will iterate thru that Dictionary and for every entry I will:
        If there is only one copy of the file, i will copy it to the Destination in a flat directory, if there is already a file by that name, I will add _ 
        to the file name until its unique.  Those files would be different photos but same name.
    If there is already a file by that name and the contents match, then I skip.


I should be able to run this program against every directory of photos that i have and ensure that I have a flattened directory of those photos with exactly
one copy.


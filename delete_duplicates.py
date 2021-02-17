import tmgshare as tmg
import sys

destination_dir = "Z:\\PhotosMaster.2"

if (len(sys.argv) == 2):
    destination_dir = sys.argv[1]
    
print("Using directory:", destination_dir)
input("Press enter to start the process")

dict_hashes = tmg.create_list_of_unique_files(destination_dir)
tmg.go_delete_duplicate(dict_hashes, destination_dir)
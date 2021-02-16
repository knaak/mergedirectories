import tmgshare as tmg

destination_dir = "Z:\\PhotosMaster.2"

dict_hashes = tmg.create_list_of_unique_files(destination_dir)
tmg.go_delete_duplicate(dict_hashes, destination_dir)

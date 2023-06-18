# Folder equality script
I made this script by request for a friend. The purpose is to check that all folders in a given folder contain the same files and subdirectories. This is made for windows cause that's what he uses, idk if it works on linux.

# Prerequisites
1. You'll need python (duh). Go install it from here:
https://www.python.org/downloads/

2. You'll need `natsort`, install that by running
`$ pip install natsort`

3. If you want to test the script but don't have a folder structure yet
I've made the script `make_a_load_of_test_folders.py` which you'll also find in this repo.
<br><br>You use it by running `$ py <path/to/script/>make_a_load_of_test_folders.py <amount_of_folders> <path_to_folders>`, where you replace the arguments.
<br><br>It'll then create as many folders as you tell it to, where all except a random one contains a text file.

4. To use the main script, simply run `$ py <path/to/script/>check_folder_equality.py <path_to_folders> <reference_folder_index>`, where you replace the arguments.
<br><br>You pick a folder that you know has the right structure, and use that as your reference.
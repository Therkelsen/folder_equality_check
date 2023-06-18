import os
import sys
import logging
from natsort import natsorted

logging.basicConfig(level=logging.INFO)

def get_all_subfolders(path_to_folder):
    """
    Recursively get all subfolders of a folder and sort them using natural sorting.

    Args:
        path_to_folder (str): Path to the folder to get subfolders from.

    Returns:
        list: A list of subfolders sorted using natural sorting.
    """
    subfolders = []
    for item in os.listdir(path_to_folder):
        item_path = os.path.join(path_to_folder, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
            subfolders.extend(get_all_subfolders(item_path))
    subfolders = natsorted(subfolders)  # Use natural sorting
    return subfolders

def get_subfolders_and_files(path_to_folder):
    """
    Get a list of subfolders and files in a folder.

    Args:
        path_to_folder (str): Path to the folder to get subfolders and files from.

    Returns:
        tuple: A tuple containing a list of subfolders and a list of files.
    """
    subfolders = []
    files = []
    for item in os.listdir(path_to_folder):
        if os.path.isdir(os.path.join(path_to_folder, item)):
            subfolders.append(item)
        else:
            files.append(item)
    return subfolders, files

def compare_folders(list_of_folders, reference_folder_index):
    """
    Compare the subfolders and files of a list of folders to a reference folder.

    Args:
        list_of_folders (list): A list of folders to compare.
        reference_folder_index (int): The index of the reference folder in the list of folders.
    """
    if len(list_of_folders) < 2:
        logging.error(" | You need to provide at least two folders to compare.")
        return

    if reference_folder_index >= len(list_of_folders):
        logging.error(" | Reference folder index is out of range.")
        return

    reference_folder = list_of_folders[reference_folder_index]
    reference_subfolders, reference_files = get_subfolders_and_files(reference_folder)
    logging.debug(" | Using %s as the reference folder to compare against.", reference_folder)
    logging.debug(" | Subfolders and files in %s: %s, %s", os.path.basename(reference_folder), reference_subfolders, reference_files)

    for folder_index, folder in enumerate(list_of_folders):
        if folder_index == reference_folder_index:
            continue
        subfolders, files = get_subfolders_and_files(folder)
        if set(subfolders) != set(reference_subfolders):
            logging.error(" | Subfolders in %s are not the same as in %s.", os.path.basename(folder), os.path.basename(reference_folder))
        if set(files) != set(reference_files):
            logging.error(" | Files in %s are not the same as in %s.", os.path.basename(folder), os.path.basename(reference_folder))

def main(path, reference_idx):
    """
    Main function to compare folders.

    Args:
        path (str): Path to the folder to compare subfolders and files.
        reference_idx (str): Index of the reference folder in the list of folders.
    """
    if not path or not reference_idx:
        logging.error(" | Missing command line arguments.")
        return

    folders_to_compare = get_all_subfolders(path)
    compare_folders(folders_to_compare, int(reference_idx))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

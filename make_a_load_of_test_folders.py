import os
import sys
import random
import logging

logging.basicConfig(level=logging.DEBUG)

def make_x_dirs_in_path(x, path):
    """
    Make x folders in a path and put a text file in all but one of them.

    Args:
        x (int): The number of folders to make.
        path (str): The path to make the folders in.
    """
    random_number = random.randint(0, x - 1)
    if not os.path.exists(path):
        os.mkdir(path)

    for dirs in os.listdir(path):
        for files in os.listdir(os.path.join(path, dirs)):
            os.remove(os.path.join(path, dirs, files))
        os.rmdir(os.path.join(path, dirs))

    for i in range(x):
        os.mkdir(os.path.join(path, "folder_{}".format(i)))
        if(random_number != i):
            with open(os.path.join(path, "folder_{}".format(i), "text_file.txt"), "w") as f:
                f.write("This is a text file in folder_{}.".format(i))
        else:
            logging.info(" | Not creating a text file in folder_{}.".format(i))

def main(amount, path):
    """
    Main function to make folders.
    
    Args:
        amount (str): The number of folders to make.
        path (str): The path to make the folders in.
    """
    logging.info(" | Creating %s folders in %s.", amount, path)
    make_x_dirs_in_path(int(amount), path)
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


import os
from utils import (create_folder, list_directory, create_text_file, delete_file)

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())

    # Create a new folder
    workspace = "my_workspace"
    create_folder(workspace)

    #show contents of this folder
    list_directory(os.getcwd())

    # Create a text file in the new folder
    create_text_file(workspace, "file-1.txt", "hI! i am file-1")
    create_text_file(workspace, "file-2.txt", "hI! i am file-2")
    create_text_file(workspace, "file-3.txt", "hI! i am file-3")

    # show contents of this folder 
    list_directory(workspace)

    #delete one file from current folder
    delete_file(workspace, "file-2.txt")

    # show updated content for this folder
    list_directory(workspace)
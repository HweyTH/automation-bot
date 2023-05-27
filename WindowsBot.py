"""
Python Script

Summary: a python automation script to clean up and sort by file types in directory

Parameters:

"""
import datetime
import os
import argparse

class WindowsBot:

    dir = ""
    fileList = []
    folderList = []
    
    def __init__(self):
        parser = argparse.ArgumentParser(description="Clean up directory and sort files by types")

        parser.add_argument("--path", type=str, default=".", help="**Directory to start clean-up")

        args = parser.parse_args()

        # extract the directory given by user
        self.dir = args.path

        print(f"Cleaning up dir: {self.dir}")

        return

    # a function to create subfolders for the correct file extensions
    def folderCreate(files):
        for file in files:
            fileRoot, fileType = os.path.splitext(file)
            fileDir = os.path.dirname(fileRoot)
            fileName = os.path.basename(fileRoot)

            print(f"File Name is {fileName}")
            print(f"File Directory is {fileDir}")
            print(f"File Type is {fileType}")
            print("----------------------------")
        return    
 







"""
Python Script

Summary: a python automation script to clean up and sort by file types in directory

Parameters:

"""
import datetime
import os
import argparse

class WindowsBot:

    dir = any
    moved = 0
    folderCreated = []
    fileList = []
    folderList = []
    
    def __init__(self, parser):
        # extract arguments given by user
        args = parser.parse_args()
        self.dir = args.path

        print(f"Cleaning up dir: {self.dir}")

        return
    
    # a function to get lists of files and folders in directory
    def dirList(self):
        # get the list of all the files and folders in the directory
        dirContent = os.listdir(self.dir)

        # create a path connecting (given) directory and files' name
        # Note: os.listdir() only supplies the names of files and folders and not the 
        # .. directory to them
        fullDir = [os.path.join(self.dir, doc) for doc in dirContent]

        # filter files and folders into two lists
        self.fileList = [file for file in fullDir if os.path.isfile(file)]
        self.folderList = [folder for folder in fullDir if os.path.isdir(folder)]

        return

    # a function to create subfolders for the correct file extensions
    def folderCreate(self, files):
        for file in files:
            fileRoot, fileType = os.path.splitext(file)
            fileDir = os.path.dirname(fileRoot)
            fileName = os.path.basename(fileRoot)

            print(f"File Name is {fileName}")
            print(f"File Directory is {fileDir}")
            print(f"File Type is {fileType}")
            print("----------------------------")

            break

        return    
 







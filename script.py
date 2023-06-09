import argparse
import os

parser = argparse.ArgumentParser(description="Clean up directory and sort files into subfolders")

parser.add_argument("--path", type=str, default=".", help="Directory to be cleaned")

args = parser.parse_args()

path = args.path

print(f"Cleaning up directory {path}")

# get all the content in the GIVEN directory
dirContent = os.listdir(path)

fullDirContent = [os.path.join(path,file) for file in dirContent]

docs = [doc for doc in fullDirContent if os.path.isfile(doc)]

folders = [dir for dir in fullDirContent if os.path.isdir(dir)]

print(f"List of documents {docs}")

print(f"List of folders {folders}")

# create variables to track list of files moved
fileNum = 0

newFolders = []

# looping through every files in the given directory
# default: script directory
for doc in docs:
    fullDir, fileExt = os.path.splitext(doc)
    fileDir = os.path.dirname(fullDir)
    fileName = os.path.basename(fullDir)

    if fileName == "script" or fileName.startswith('.'):
        continue

    print(fullDir)
    print(fileExt)
    print(fileDir)
    print(fileName)

    # create a subfolder directory to move files into
    subDir = os.path.join(path, fileExt[1:].lower())

    # check if the sub-folders already existed in the directory
    if subDir not in folders and subDir not in newFolders:
        try:
            # if file not existed, create the appropriate sub-folders
            os.mkdir(subDir)
            newFolders.append(subDir)
            print(f"A subfolder {subDir} has been created")
        except FileExistsError as error:
            print(f"A relevant subfolder already existed in the directory {error}")

    # create a new directory for the moving file(s)
    newPath = os.path.join(subDir, fileName) + fileExt
    # os.path.rename(doc, newPath)
    fileNum += 1
    
    print(f"Moved file {doc} to {newPath}")

print(f"Finished moving {fileNum} files into {len(newFolders)} folders")


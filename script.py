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





     
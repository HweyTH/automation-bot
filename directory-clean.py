"""
Python Script

Summary: a python automation script to clean up and sort by file types in directory

Parameters:

"""
import datetime
import os
import argparse

def argParse():
    parser = argparse.ArgumentParser(description="Clean up directory and sort files by types")

    parser.add_argument("--path", type=str, default=".", help="**Directory to start organizing**")

    args = parser.parse_args()

    path = args.path

    print(f"Cleaning up directory {path}")

def main():
    argParse()



# Finding Files

# For this problem, the goal is to write code for finding all files under a
# directory (and all directories beneath it) that end with ".c"

import os

def find_files(suffix, path):

    matches = []

    if os.path.isdir(path):
      for listing in os.scandir(path):
        matches += find_files(suffix, listing.path)

    elif path.endswith(suffix):
        matches.append(path)

    return matches

folder = "../testdir"
print (find_files(".c", folder))

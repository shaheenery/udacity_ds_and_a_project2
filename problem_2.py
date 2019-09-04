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

# Test C source files
print (find_files(".c", folder))
# ['../testdir/subdir3/subsubdir1/b.c', '../testdir/t1.c', '../testdir/subdir5/a.c', '../testdir/subdir1/a.c']

# Test C header files
print (find_files(".h", folder))
# ['../testdir/subdir3/subsubdir1/b.h', '../testdir/subdir5/a.h', '../testdir/t1.h', '../testdir/subdir1/a.h']

# Edge Case test with no file found
print (find_files(".js", folder))
# []

# Edge Case test with system hidden file
print (find_files(".gitkeep", folder))
# ['../testdir/subdir4/.gitkeep', '../testdir/subdir2/.gitkeep']

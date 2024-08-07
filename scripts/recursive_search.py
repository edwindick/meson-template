# Searches and records all files within a given directory
# recursive_search.py <dir>

import sys, os


argv_len = len(sys.argv)
if argv_len < 2:
    print("Invalid number of arguments.")
    sys.exit(-1)

parent_dir = sys.argv[1]
if not os.path.exists(parent_dir):
    print("Specified directory does not exist.")
    sys.exit(-2)

found_files = []
for dirpath, dirnames, filenames in os.walk(parent_dir):
    for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            found_files.append(file_path)

for file in found_files:
    print(file)

# Copys a set of files to specified directory
# copy_to.py <dest> [<src1> <src2> ...]

import sys, os, shutil


argv_len = len(sys.argv)
if argv_len < 3:
    sys.exit(-1)

out_dir = sys.argv[1]
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for file in range(2, argv_len):
    shutil.copy(sys.argv[file], out_dir)

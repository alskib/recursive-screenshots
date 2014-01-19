import os
import sys
import errno


#rootdir = os.getcwd()
# don't forget to escape backslash and spaces
rootdir = "H:\\In\ and\ Out"
mtnbinary = "C:\\Users\\franklin\\Downloads\\mtn-200808a-win32\\mtn.exe"
switches = " -P -h 0 -c 3 -r 5 -w 1024 -g 0 -j 80 -b 0.80 -D 12 -L 4:2 -k 000000 -o .jpg"
switchOutputDir = " -O " + rootdir + "\\_covers "
mtnCmd = mtnbinary + switches + switchOutputDir

try:
    os.makedirs(rootdir + "\\covers")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

for root, subfolders, files in os.walk(rootdir):
    for f in files:
        if f.endswith(".mkv") \
        or f.endswith(".avi") \
        or f.endswith(".mp4") \
        or f.endswith(".wmv") \
        or f.endswith(".mpg") \
        or f.endswith(".mpeg") \
        or f.endswith(".flv"):
            os.system(mtnCmd + "\"" + os.path.join(root, f) + "\"")

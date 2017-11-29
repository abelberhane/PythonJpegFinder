import os, glob

os.chdir("/Users/Abel/Desktop/Sample")
for file in glob.glob("*.jpg"):
    print(file)
import sys,os
import glob


def each_line(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\r\n')

ego=sys.argv[1]
target={}

for line in each_line(ego):
    target[line]=1

files = glob.glob("following/*")
for file in files:
    user =os.path.basename(file)
    user=os.path.splitext(user)[0]
    if user in target:
        for line in each_line(file):
            if line in target:
                print (user,line)

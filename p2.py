import os
filespath = '//Users/gongjie/Desktop/pythonstudy/test1/Project1/PracticeNeed/files'
files = os.listdir(filespath)
#print(files)
for f in files:
    if not f.endswith('.gif'):
        #print(f)
        if('project30' in f or 'commerical' in f):
            print(f)
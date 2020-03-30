import os
import shutil
path = '//Users/gongjie/Desktop/pythonstudy/test1/Project2/PracticeNeed/problem2_files'


#makeimagefiles()
imagepath = path+'/images'
print(imagepath)
if not os.path.exists(imagepath):
    os.makedirs(imagepath)
#makeducoument()

documentpath = path +'/document'
print(documentpath)
if not os.path.exists(documentpath):
    os.makedirs(documentpath)

files = os.listdir(path)
for f in files:
    if(f.split('.')[-1] =='jpg' or f.split('.')[-1]=='png' or f.split('.')[-1]=='gif'):
        f1path = path + '/'+f.split('.')[-1]
        f1files = os.listdir(f1path)
        for f1 in f1files:
            f1srcpath = f1path+'/'+f1
            shutil.move(f1srcpath, imagepath)
    if(f.split('.')[-1]=='doc' or f.split('.')[-1]=='docx ' or f.split('.')[-1]=='ppt' or f.split('.')[-1]=='md'):
        f2path = path + '/' + f.split('.')[-1]
        f2files = os.listdir(f2path)
        for f2 in f2files:
            f2srcpath = f2path + '/' + f2
            shutil.move(f2srcpath, documentpath)
    #movetoducoument()
print('move ok!!!')
shutil.rmtree(imagepath)

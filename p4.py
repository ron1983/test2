import os
f2 = []
filepath = '//Users/gongjie/Desktop/pythonstudy/problem3_files'
for root,dirs,files in os.walk(filepath):
    for f in files:
        if f not in f2:
            f2.append(f)
        else:
            os.remove(os.path.join(root,f))
print(f2)
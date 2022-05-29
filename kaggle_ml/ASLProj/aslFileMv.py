from os import *
import shutil
import random

rdir = "C:\\Users\\ronit\\Programming\\AI\\kaggle_data\\ASL\\asl_alphabet_train"
newDir = "C:\\Users\\ronit\\Programming\\AI\\kaggle_data\\ASL\\asl_alphabet_validation"

for subdir, dirs, files in walk(rdir):
    for path, names, fnames in walk(subdir):
        for file in fnames:
            n = round(random.uniform(1.0,100.0))
            if n < 12:
                name = ""
                if file[0] == 'd': name = "\\" + "del"
                elif file[0] == 'n': name = "\\" + "nothing"
                elif file[0] == 's': name = "\\" + "space"
                else: name = "\\" + file[0]
                
                name += "\\" + file
                #print(rdir+name, newDir+name)
                shutil.move(rdir + name, newDir + name)
                # shutil.move(newDir + name, rdir + name)
    print("_________________________")
# PythonTestFile.py
import os

to_Find = {
    "Number of MUs": ['/', 'nopuncdata'],
    "Meaningless MUs": ['(?i)/like/|/um/|/ah/|/well/|/so/','nopunclinedata'], 
    "I think": ['Ithink|Ithought|Ihadthought','nopunclinedata'],
    "I": [' I | I\'','data'],
    "we": ['(?i) we | we\'','data'],
    "Questions": ['\?','data'], 
    }

for key in to_Find:
    print key



FileName = r'C:/Users/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + '1' + '/SinglePersonTexts/'

print os.listdir(FileName)
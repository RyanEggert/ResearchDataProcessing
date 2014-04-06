# DiscourseAnalysisChecker.py

import os


TeamNumber = 1
FileName = r'C:/Users/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + str(TeamNumber) + '/SinglePersonTexts/'

Files = os.listdir(FileName)

for s in Files:
    counter = 0
    textfile = open(FileName +s)  # open the singe-person text file
    data = textfile.read()
    textfile.close()
    nopuncdata = data.translate(None, ";',.? !-")
    for s2 in nopuncdata.splitlines():
        counter +=1
        if not s2.endswith('/'):
            print s
            print 'ln. '+ str(counter) + '  :   ' + s2
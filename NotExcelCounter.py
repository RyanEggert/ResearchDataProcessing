# NotExcelCounter.py

print "Start"
import re

TeamNumber = 3
PersonName = 'Alyssa Little'
pname = PersonName.lower()
                         # Ensure all characters in name are lowercase (naming
                         # scheme)
procPersonName = pname.replace(" ", "")  #

# Assemble the textfile filepath
FileName = r'C:/Users/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + \
    str(TeamNumber) + '/SinglePersonTexts/' + str(procPersonName) + '.txt'

textfile = open(FileName)  # open the singe-person text file

data = textfile.read()

textfile.close()
nopuncdata = data.translate(None, ";',.? !")


SearchTerm = '/(like|um|ah)/'

for matchstr in re.findall(SearchTerm, nopuncdata):
    print matchstr

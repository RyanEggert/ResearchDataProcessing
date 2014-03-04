# NotExcelCounter.py

print "Start"
import re


def Search_name_for(TeamNumber, PersonName, SearchTerm):

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

    return len(re.findall(SearchTerm, nopuncdata))

    # for matchstr in re.findall(SearchTerm, nopuncdata):
    #     print matchstr


toFind = '/like/'
toFind = '/'

TeamMembers = ['Alyssa Little', 'Diana Pitkaranta', 'Lawrence Lee', 'Tom Dominski', 'Trevor Able']

for x in range(len(TeamMembers)):
    Count = Search_name_for(3, TeamMembers[x], toFind)
    print TeamMembers[x] + '   ' + str(Count)

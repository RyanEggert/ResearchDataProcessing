# DiscourseAnalysisCounter.py
import re  # Import regular expressions module

##################FUNCTION-DEFINITION##################


def Search_name_for(TeamNumber, PersonName, SearchTerm):
    """Finds a text transcript of a specific team's member. Searches for the regex SearchTerm"""
    pname = PersonName.lower()
     # Ensure all characters in name are lowercase (naming
     # scheme)
    procPersonName = pname.replace(" ", "")  #

    # Assemble the textfile filepath
    
    FileName = r'/home/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + \
        str(TeamNumber) + '/SinglePersonTexts/' + str(procPersonName) + '.txt'


    # FileName = r'C:/Users/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + \
    #     str(TeamNumber) + '/SinglePersonTexts/' + str(procPersonName) + '.txt'


        #Change first part of filepath to reflect user's dropbox location

    textfile = open(FileName)  # open the singe-person text file

    data = textfile.read()

    textfile.close()
    
    nopuncdata = data.translate(None, ";',.? !")  # Deletes the characters enclosed in double quotes from data and saves as nopuncdata
    nopunclinedata = nopuncdata.replace('\r', '').replace('\n','')  # Remove carriage returns and newline characters

    return len(re.findall(SearchTerm, data))  # Switch nopuncdata with data or nopunclinedata

    # for matchstr in re.findall(SearchTerm, nopuncdata):
    #     print matchstr
    # above is from concordancer program. Something of this form can be used to display context of identified areas

#########################BEGIN#########################


toFind = '(?i) we | we\'' # Regular Expression input. (?i) is case insensitive

TeamMembers = ['Alyssa Little', 'Diana Pitkaranta', 'Lawrence Lee', 'Tom Dominski', 'Trevor Able']  # List of team members. Change to reflect current team

for x in range(len(TeamMembers)):
    Count = Search_name_for(3, TeamMembers[x], toFind)
    print TeamMembers[x] + '   ' + str(Count)

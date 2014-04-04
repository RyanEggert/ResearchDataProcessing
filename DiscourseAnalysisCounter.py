# DiscourseAnalysisCounter.py
import re  # Import regular expressions module

#  Be sure to replace apostrophe character with ' in all text files before proceeding.


##################FUNCTION-DEFINITION##################


def Search_name_for(TeamNumber, PersonName, SearchTerm, DataToSearch):
    """Finds a text transcript of a specific team's member. Searches for the regex SearchTerm"""
    pname = PersonName.lower()
     # Ensure all characters in name are lowercase (naming
     # scheme)
    procPersonName = pname.replace(" ", "")  #

    # Assemble the textfile filepath
    
    # FileName = r'/home/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + \
        # str(TeamNumber) + '/SinglePersonTexts/' + str(procPersonName) + '.txt'


    FileName = r'C:/Users/reggert/Dropbox/Discourse Files 2013-2014/Analysis/Team ' + \
         str(TeamNumber) + '/SinglePersonTexts/' + str(procPersonName) + '.txt'


        #Change first part of filepath to reflect user's dropbox location

    textfile = open(FileName)  # open the singe-person text file

    data = textfile.read()

    textfile.close()
    
    nopuncdata = data.translate(None, ";',.? !")  # Deletes the characters enclosed in double quotes from data and saves as nopuncdata
    nopunclinedata = nopuncdata.replace('\r', '').replace('\n','')  # Remove carriage returns and newline characters

    return len(re.findall(SearchTerm, eval(DataToSearch)))  # return total number of found instances of SearchTerm

    # for matchstr in re.findall(SearchTerm, nopuncdata):
    #     print matchstr
    # above is from concordancer program. Something of this form can be used to display context of identified areas

#########################BEGIN#########################


toFind = '(?i)/like/|/um/|/ah/|/well/|/so/' # Regular Expression input. (?i) is case insensitive

TeamMembers = ['Eric Abramson', 'John Powers', 'Ruth Thompson', 'Mary Gothel', 'Mark Castellani']  # List of team members. Change to reflect current team

for x in range(len(TeamMembers)):
    
    Count = Search_name_for(1, TeamMembers[x], toFind, 'nopunclinedata')  # Choose data, nopuncdata, or nopunclinedata
    
    print TeamMembers[x] + '|' + str(Count)  # Output counted and labeled data for copying directly into MS Excel

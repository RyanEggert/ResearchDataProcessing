# DiscourseAnalysisCounter.py
import re  # Import regular expressions module

#  Be sure to replace apostrophe character with ' in all text files before proceeding.


##################FUNCTION-DEFINITIONS##################


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
    
    nopuncdata = data.translate(None, ";',.? !-")  # Deletes the characters enclosed in double quotes from data and saves as nopuncdata
    nopunclinedata = nopuncdata.replace('\r', '').replace('\n','')  # Remove carriage returns and newline characters

    return len(re.findall(SearchTerm, eval(DataToSearch)))  # return total number of found instances of SearchTerm

    # for matchstr in re.findall(SearchTerm, nopuncdata):
    #     print matchstr
    # above is from concordancer program. Something of this form can be used to display context of identified areas



def LoopThroughTeam(toFind, inWhichData, teamNum, teamMembers, categoryTitle):
    print categoryTitle

    for x in range(len(teamMembers)):
    
        Count = Search_name_for(teamNum, teamMembers[x], toFind, inWhichData)  # Choose data, nopuncdata, or nopunclinedata
        
        print teamMembers[x] + '|' + str(Count)  # Output counted and labeled data for copying directly into MS Excel
    print 2*'\n'  


#########################BEGIN##########################

to_Find = {
    "Number of MUs": ['/', 'nopuncdata'],
    "Meaningless MUs": ['(?i)/like/|/um/|/ah/|/well/|/so/','nopunclinedata'], 
    "I think": ['Ithink|Ithought|Ihadthought','nopunclinedata'],
    "I": [' I | I\'','data'],
    "we": ['(?i) we | we\'','data'],
    "Questions": ['\?','data'], 
    "Agreement": ['(?i)yes|yeap|yeah|yup|uhhuh','nopuncdata'],
    "Disagreement": ['(?i)no/|no |nope', 'data'],
    }


Team_Members = ['Eric Abramson', 'John Powers', 'Ruth Thompson', 'Mary Gothel', 'Mark Castellani']  # List of team members. Change to reflect current team

for key in to_Find:
    LoopThroughTeam(to_Find[key][0], to_Find[key][1], 1, Team_Members, key)
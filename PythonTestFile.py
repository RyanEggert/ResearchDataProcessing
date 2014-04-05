# PythonTestFile.py


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
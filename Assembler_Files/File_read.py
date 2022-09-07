import os
#import fileinput
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'MOT.csv')

#with open('MOT.csv','r') as mot_file:
#    for lines in mot_file:
#        print(lines.rstrip())

# def mot_file_iterator():
#     dirname = os.path.dirname(__file__)
#     filename = os.path.join(dirname, 'MOT.csv')

#     mot_file = open(filename, 'r')

#     return fileinput.input(mot_file)

def return_Mot():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'MOT.csv')
        
    with open(filename,'r') as mot_file:
        for lines in mot_file:
            #print(lines.rstrip())
            yield lines.rstrip()
   
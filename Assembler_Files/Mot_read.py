import os
#import fileinput
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'MOT.csv')
#print(dirname)
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
        #ignore first line
        
        next(mot_file)
        
        for lines in mot_file:
            #print(lines.rstrip())
            yield lines.rstrip()

def Mot_dict():
    #Mnemonics,Opcode,Size,Type,Subroutine
    dict_key = ['Mnemonics','Opcode','Size','Type','Subroutine']
    for line in return_Mot():
        list = line.rstrip().split(',')
        dict_y = dict(zip(dict_key,list))
        
        #Opcode convert to integer
        # if dict_y['Opcode'] == '':
        #     dict_y['Opcode'] = dict_y.get('Opcode', None)
        # else:
        #     dict_y['Opcode'] = dict_y.get('Opcode', int(dict_y['Opcode']))
            
        # #Size convert to integer
        # if dict_y['Size'] == '_':
        #     dict_y['Size'] = dict_y.get('Size', None)
        # else:
        #     dict_y['Size'] = dict_y.get('Size', int(dict_y['Size']))
            
        yield dict_y

def isMnemonics(mnemonic):
    for mot in Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return True
    return False

for a in Mot_dict():
    print(a)

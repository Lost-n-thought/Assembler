import os
from types import GeneratorType


def return_Mot() -> GeneratorType:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'MOT.tsv')
    
    with open(filename,'r' , encoding='utf-8-sig') as mot_file:
        #ignore first line
        # next(mot_file)
        
        # set global variable mot_dict_key
        #mot_dict_key  is first line of MOT.csv , containing names of columns
        global mot_dict_key
        mot_dict_key = mot_file.readline().rstrip().split('\t')       
        
        for lines in mot_file:
            #print(lines.rstrip())
            yield lines.rstrip()

def Mot_dict(): #dict generator
    #Mnemonics,Opcode,Size,Type,Subroutine
    #mot_dict_key = ['Mnemonics','Opcode','Size','Type','Subroutine']
    for line in return_Mot():
        list = line.rstrip().split('\t')
        dict_y = dict(zip(mot_dict_key,list))
        
        #Opcode convert to integer
        if dict_y['Opcode'] == '':
            dict_y['Opcode'] = None
        else:
            dict_y['Opcode'] = int(dict_y['Opcode'])
            
        #Size convert to integer
        if dict_y['Size'] == '_':
            dict_y['Size'] = None
        else:
            dict_y['Size'] = int(dict_y['Size'])
            
        # set empty subroutine to None  
        yield dict_y
        
# checks if Mnemonics is in MOT
def isMnemonics(mnemonic: str):
    for mot in Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return True
    return False

#Gets Attributes(any field fo given mnemonics) for given Mnemonics
def get_Mnemonics_attribute(mnemonic :str , attribute : str = 'Size'):

    if attribute not in next(Mot_dict()):
        raise Exception('Attribute {} not in mot_dict_key'.format(attribute) )
    if isMnemonics(mnemonic) is False:
        raise Exception('Mnemonic {} not in MOT'.format(mnemonic))
    
    for mot in Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return mot[attribute]


# return dict will all attributes for given Mnemonics
def return_given_mnemonics_dict(mnemonic :str) -> dict:
    for mot in Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return mot
    else:
        raise Exception('Mnemonic {} not in MOT'.format(mnemonic))
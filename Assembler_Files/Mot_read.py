import os
from types import GeneratorType

registers_name = ['AREG', 'BREG', 'CREG', 'DREG']
Branch_condition = ['LE' , 'LT' , 'ET' , 'GT' , 'GE']

def _return_Mot() -> GeneratorType:
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

def _Mot_dict() ->GeneratorType: #dict generator
    #Mnemonics,Opcode,Size,Type,Subroutine
    #mot_dict_key = ['Mnemonics','Opcode','Size','Type','Subroutine']
    for line in _return_Mot():
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
 
 
 # Public Methods
 
        
# checks if Mnemonics is in MOT
def isMnemonics(mnemonic: str , caseLess = False) -> bool:
    for mot in _Mot_dict():
        if (caseLess == False):
            if mot['Mnemonics'] == mnemonic:
                return True
        elif (caseLess == True):
            if mot['Mnemonics'].casefold() == mnemonic.casefold():
                return True
    return False


#checks if word is protected
def is_word_protected(word :str , caseLess  :bool = False , check_for_Mnemonics :bool = False ,) -> bool:
    if check_for_Mnemonics == True:
        if isMnemonics(word , caseLess) == True:
            return True
        
    if (caseLess == False):
        if word in Branch_condition:
            return True
        if word in registers_name:
            return True
    elif (caseLess == True):
        for reg in registers_name:
            if word.casefold() == reg.casefold() :
                return True  
        for cond in Branch_condition:
            if word.casefold() == cond.casefold():
                return True        
    return False


#Gets Attributes(any field fo given mnemonics) for given Mnemonics
def get_Mnemonics_attribute(mnemonic :str , attribute : str = 'Size'):

    if attribute not in next(_Mot_dict()):
        raise Exception('Attribute {} not in mot_dict_key'.format(attribute) )
    if isMnemonics(mnemonic) is False:
        raise Exception('Mnemonic {} not in MOT'.format(mnemonic))
    
    for mot in _Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return mot[attribute]


# return dict will all attributes for given Mnemonics
def return_given_mnemonics_dict(mnemonic :str) -> dict:
    for mot in _Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return mot
    else:
        raise Exception('Mnemonic {} not in MOT'.format(mnemonic))
    

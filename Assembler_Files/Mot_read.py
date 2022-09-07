import os


def return_Mot():
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

def Mot_dict():
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

def isMnemonics(mnemonic):
    for mot in Mot_dict():
        if mot['Mnemonics'] == mnemonic:
            return True
    return False

def get_Mnemonics_attribute(mnemonic , attribute = 'Size'):
    for mot in Mot_dict():
        if attribute not in mot_dict_key:
            raise Exception('Attribute not in mot_dict_key')
        if mot['Mnemonics'] == mnemonic:
            return mot[attribute]
    return None


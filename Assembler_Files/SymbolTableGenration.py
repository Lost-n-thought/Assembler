import fileinput as fi
import os

# protected keywords
# 1. Branch condition [LE , LT , ET , GT , GE]
# 2. Registers Name [AREG, BREG, CREG, DREG]

#symbols 2 types of symbols
# 1. DC DL type symbols  - Variable -> DataAddress
# 2. Label type symbols -  Address  -> StatementAddress

# main purpose
# input given Symbol , declare/Used , Type?
#
# functions used
    #create_symbol_Table
    #symbol_used
        #used_as_Address (in jump)
        #used_as_Variable (in DC and IS statement like ADD , MOVE)
    #symbol_defined
        #defined_as_Address (in jump)
        #defined_as_Variable (in DC and IS statement like ADD , MOVE)
    #symbol_table_done () #to be used at the end of the program
        #returns True if all symbols are defined
        #returns False if not all symbols are defined
        
        #Give Warning if symbol is defined but not used



# Internal Functions

    # def symbol_defined(symbol , Address , used_as , LineNo ):   
    # check if symbol already exits ? 
    # yes   ->  isDeclared = True   -> Exception
    #       ->  isDeclared = False  -> usedAs != usedAs -> Exception
    #                               usedAs == usedAs -> Change isDeclared to True(changing)
    #                                                   and add Address
    # No   ->  Add entry to symbol table(append)

    # def symbol_used(symbol , used_as , LineNo):
    # check if symbol already exits ? 
    # yes  ->   usedAs != usedAs -> Exception
    #           usedAs == usedAs -> isUsed = True    -> do nothing
    #                               isUsed = False   -> Change to True (changing)
    # no  -> add entry  (Appending)  
    
# sample Symbol table

# Symbol, Address(number or blank''), isDeclared(True or False), isUsed(True or False),
# UsedAs(Variable or Address), (separated by tab)
symbol_dict_key = ['Symbol', 'Address', 'isDeclared', 'isUsed' , 'UsedAs']

Branch_condition = ['LE' , 'LT' , 'ET' , 'GT' , 'GE']
Registers_Name = ['AREG', 'BREG', 'CREG', 'DREG']


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../temp', 'SymbolTable.tsv')

#checks if symbol used is protected 
def is_symbol_protected(symbol :str) -> bool:
    return symbol in Branch_condition or symbol in Registers_Name

#checks if symbol used is protected and if it is raised exception
def symbol_protected_check(symbol :str , LineNo :int):
    if is_symbol_protected(symbol):
        raise Exception('{} Symbol used in lineno {} is protected keyword '
            ''.format(symbol, LineNo))




def create_symbol_table():
    with open(filename, 'w', encoding='utf-8-sig'):
        pass


def convert_line_to_dict(line):
    return dict(zip(symbol_dict_key, line.rstrip().split('\t')))
   
def convert_dict_into_line(dict):
    return '\t'.join([str(dict[key]) for key in symbol_dict_key])

#gives a  line_dict
def symbol_line_lineDict(symbol):
    with open(filename, 'r', encoding='utf-8-sig') as symbol_file:
        for line in symbol_file:
            line = convert_line_to_dict(line)
            if line['Symbol'] == symbol:
                return line
    return None

def is_symbol_declared(line_dict :dict) -> bool:
    return line_dict['isDeclared'] == 'True'

def is_symbol_used(line_dict :dict) -> bool:
    return line_dict['isUsed'] == 'True'

def is_symbol_variable(line_dict :dict) -> bool:
    return line_dict['UsedAs'] == 'Variable'

def is_symbol_address(line_dict :dict) -> bool:
    return line_dict['UsedAs'] == 'Address'



def append_line(line_dict :dict):
    with open(filename, 'a', encoding='utf-8-sig') as symbol_file:
        symbol_file.write(convert_dict_into_line(line_dict) + '\n')

def change_line(line_dict :dict):
    testfile = fi.FileInput(filename , inplace=True)

    for line in testfile:
        if(convert_line_to_dict(line)['Symbol'] == line_dict['Symbol']):
            print(convert_dict_into_line(line_dict))
        else:
            print(line.rstrip())
    testfile.close()





def symbol_defined(symbol :str, Address :int , used_as :str , LineNo :int = None):
    
    symbol_protected_check(symbol, LineNo)
    line_dict = symbol_line_lineDict(symbol)
    
    if line_dict is None:#symbol not found
        line_dict = {'Symbol':symbol, 'Address':str(Address), 'isDeclared':'True', 'isUsed':'False', 'UsedAs':used_as}
        # add new entry to symbol table(append)
        append_line(line_dict)
                         
    else:#symbol found
        if (line_dict['isDeclared'] == 'True'):
            raise Exception('"{}" - Symbol already declared ,it is '
            'declared again in line {}'.format(symbol , LineNo))
        
        if(line_dict['UsedAs'] != used_as):
            raise Exception('Type not matched "{}" - Symbol already used as {} ,it is '
                'used again as {} in line {}'.format(symbol , line_dict['UsedAs'] , used_as , LineNo))
        
        # change isDeclared to True and add Address to existing line
        line_dict['isDeclared'] = 'True'
        line_dict['Address'] = str(Address)
        change_line(line_dict)


def symbol_used(symbol :str, used_as :str , LineNo :int = None):
    symbol_protected_check(symbol, LineNo)
    line_dict = symbol_line_lineDict(symbol)
    
    if line_dict is None:#symbol not found
        line_dict = {'Symbol':symbol, 'Address':'', 'isDeclared':'False', 'isUsed':'True', 'UsedAs':used_as}
        # add new entry to symbol table(append)
        append_line(line_dict)
                         
    else:#symbol found
        if (line_dict['UsedAs'] != used_as):
            raise Exception('Type not matched "{}" - Symbol already used  as {},it is '
            'used again in line {} as {}'.format(symbol,line_dict['UsedAs'], LineNo , used_as))
        
        # change isUsed to True in existing line
        line_dict['isUsed'] = 'True'
        change_line(line_dict)

# line = 'A\t1\tTrue\tFalse\tVariable\n'
# print(convert_line_to_dict(line))

#create_symbol_table()

#symbol_defined('A', 1, 'Variable' , 33)
#symbol_used('A', 'Address' , 33)
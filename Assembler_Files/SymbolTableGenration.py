import fileinput as fi
import os

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




# Internal Functions

    # def symbol_defined(symbol , ):   
    # check if symbol already exits ? 
    # yes  ->  isDeclared = True -> Exception
    #    ->  isDeclared = False -> change to True
    # no  -> add entry

    # def symbol_used(symbol):
    # check if symbol already exits ? 
    # yes  ->  isUsed = True    -> do nothing
    #          isUsed = False   -> Change to True
    # no  -> add entry    
    
# sample Symbol table

# Symbol, Address, isDeclared(True or False), isUsed(True or False),
# UsedAs(Variable or Address), (separated by tab)
symbol_dict_key = ['Symbol', 'Address', 'isDeclared', 'isUsed' , 'UsedAs']


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../temp', 'SymbolTable.tsv')



def create_symbol_table():
    with open(filename, 'w', encoding='utf-8-sig'):
        pass


def convert_line_to_dict(line):
    return dict(zip(symbol_dict_key, line.rstrip().split('\t')))
   
def convert_dict_into_line(dict):
    return '\t'.join([str(dict[key]) for key in symbol_dict_key])

# gives a list of [LineNo, line_dict]
def symbol_line_lineNo_lineDict_list(symbol):
    with open(filename, 'r', encoding='utf-8-sig') as symbol_file:
        for line_no ,line in enumerate(symbol_file):
            line = convert_line_to_dict(line)
            if line['Symbol'] == symbol:
                return [line_no+1, line]
    return None

def is_symbol_declared(line_dict :dict):
    return line_dict['isDeclared'] == 'True'

def is_symbol_used(line_dict :dict):
    return line_dict['isUsed'] == 'True'

def is_symbol_variable(line_dict :dict):
    return line_dict['UsedAs'] == 'Variable'

def is_symbol_address(line_dict :dict):
    return line_dict['UsedAs'] == 'Address'

def symbol_defined(symbol , used_as):
    
# def symbol_line_change()

# def symbol_declaration(symbol):
#     if check_if_symbol_exists(symbol) is False:
#         with open(filename, 'a', encoding='utf-8-sig') as symbol_file:
#             symbol_file.write(symbol + '\tTrue\tFalse\n')




line = 'A\t1\tTrue\tFalse\tVariable\n'
print(convert_line_to_dict(line))
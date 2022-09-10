import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../temp', 'SymbolTable.tsv')


# sample Symbol table
# Symbol Address isDeclared(True or False) isUsed(True or False) (separated by tab)


def is_symbolFile_empty():
    with open(filename,'r' , encoding='utf-8-sig') as symbol_file:
        if symbol_file.readline() == '':
            return True
    return False

def check_if_symbol_exists(symbol):
    with open(filename,'r' , encoding='utf-8-sig') as symbol_file:
        for line in symbol_file.readline().rstrip().split('\t'):
            if line[0] == symbol:
                return True
    return False

def symbol_declaration(symbol):
    if check_if_symbol_exists(symbol) is False:
        with open(filename,'a' , encoding='utf-8-sig') as symbol_file:
            symbol_file.write(symbol + '\tTrue\tFalse\n')
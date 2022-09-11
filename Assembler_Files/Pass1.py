import AssemblyRead as AR
import SymbolTableGenration as SG
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../temp', 'IC.txt')

def _convert_dict_to_line(dict1 :dict ,remove_line_no :bool= False):
    if(remove_line_no):
        return '\t'.join([str(dict1[key]) for key in dict1 if key != 'line_number'])
    return '\t'.join([str(dict1[key]) for key in dict1.keys()])

def create_IC_file():
    with open(filename, 'w'):
        pass

def _IC_append_line(line_dict :dict , remove_line_no :bool= False):
    with open(filename, 'a') as symbol_file:
        symbol_file.write(_convert_dict_to_line(line_dict , remove_line_no) + '\n')
        
        
SG.create_symbol_table()
create_IC_file()

for line11 in AR.final_asm_line_dict_list('sampleAssembly.asm'):
    _IC_append_line(line11[0] , True)

# for line11 in AR.final_asm_line_dict_list('sampleAssembly.asm'):
#     print(_convert_dict_to_line(line11[0]))
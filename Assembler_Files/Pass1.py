import AssemblyRead as AR
import SymbolTableGenration as SG
import os


dirname = os.path.dirname(__file__)
fileIC = os.path.join(dirname, '../temp', 'IC.txt')
fileST = os.path.join(dirname, '../temp', 'SymbolTable.tsv')


def _convert_dict_to_line(dict1 :dict ,remove_line_no :bool= False):
    if(remove_line_no):
        return '\t'.join([str(dict1[key]) for key in dict1 if key != 'line_number'])
    return '\t'.join([str(dict1[key]) for key in dict1.keys()])

def create_IC_file():
    with open(fileIC, 'w'):
        pass

def _IC_append_line(line_dict :dict , remove_line_no :bool= False):
    with open(fileIC, 'a') as symbol_file:
        symbol_file.write(_convert_dict_to_line(line_dict , remove_line_no ) + '\n')
        

# UsedAs(Variable or Address), (separated by tab)
def append_header():
    with open(fileIC, 'r') as IC_file:
        lines = IC_file.readlines()
        lines.insert(0, 'LC\tMnemonics\tOperand1\tOperand2\n')
    with open(fileIC, 'w') as IC_file:
        IC_file.writelines(lines)
    with open(fileST, 'r') as ST_file:
        lines = ST_file.readlines()
        lines.insert(0,'Symbol\tAddress\tisDeclared\tisUsed\tUsedAs\n' )
    with open(fileST, 'w') as ST_file:
        ST_file.writelines(lines)    
    
SG.create_symbol_table()
create_IC_file()

for line11 in AR.final_asm_line_dict_list('sampleAssembly.asm'):
    _IC_append_line(line11[0] , True)

append_header()

# for line11 in AR.final_asm_line_dict_list('sampleAssembly.asm'):
#     print(_convert_dict_to_line(line11[0]))
import AssemblyRead as AR
import Mot_read as MR

asm_name = 'sampleAssembly.asm'

#check if starting command is correct IE "START"
def _starting_command(first_line):
    LC = None
    
    if (first_line[1]['Mnemonics'] != 'START'):
        raise Exception('Error in line {}. ASM\
            should start with "START" command'.format(first_line[0]['line_number']))
    
    if(first_line[1]['Operand1'] is None):
        LC = 0
    if(first_line[1]['Operand1'].isdigit()):
        LC = int(first_line[1]['Operand1'])
        if(LC < 0):
            raise Exception('Error in line {}. LC should be positive'.format(first_line[0]['line_number']))
    return LC  

# returns Add LC field in 1st dict_list eg
# [{'line_number': 12, 'LC': 401}, {'label': 'NUMBER', 'Mnemonics': 'DC', 'Operand1': '5', 'Operand2': None}]
# [{'line_number': 13, 'LC': 411}, {'label': 'ARRAY', 'Mnemonics': 'DS', 'Operand1': '10', 'Operand2': None}]       
def LC_processing(asmfile_iter):
    
    LC = None
    first_line = next(asmfile_iter)
    LC = _starting_command(first_line)
    #print(LC)
    LCoriginal = LC
    for line in asmfile_iter:
        if(line[1]['Mnemonics'] == 'DC'):
            LC += 1
        elif(line[1]['Mnemonics'] == 'DS'):
            if(line[1]['Operand1'].isdigit()):
                LC += int(line[1]['Operand1'])
            else:
                raise Exception('Error in line {}. DS should have a number as operand'.format(line[0]['line_number']))
        elif(line[1]['Mnemonics'] == 'ORG'):
            if(line[1]['Operand1'].isdigit() and int(line[1]['Operand1']) >= 0):
                LC = int(line[1]['Operand1'])
            else:
                raise Exception('Error in line {}. ORG should have a +ve number as operand'.format(line[0]['line_number']))
        else:
            LC += int(MR.get_Mnemonics_attribute(line[1]['Mnemonics']))
        line[0]['LC'] = line[0].get('LC', LCoriginal)
        LCoriginal = LC
        yield line


# for a in LC_processing(asm_name):
#     print(a)
import AssemblyRead as AR
import Mot_read as MR

asm_name = 'sampleAssembly.asm'

#check if starting command is correct IE "START"
def starting_command(first_line):
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

        
def LC_processing(asm_name):
    asmfile_iter =AR.final_asm_line_dict(asm_name)
    LC = None
    first_line = next(asmfile_iter)
    LC = starting_command(first_line)
    #print(LC)
    
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

        line[0]['LC'] = line[0].get('LC', LC)
        yield line


# for a in LC_processing(asm_name):
#     print(a)
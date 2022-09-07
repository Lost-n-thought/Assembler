import os
import re
import Mot_read as mr

registers_name = ['AREG', 'BREG', 'CREG', 'DREG']

# A iterator that returns [line number , line] for each line in the file.
# Ignore empty lines and lines starting with a '#'
def assembler_iter(file_name):
    """
    Iterates through the lines of the assembly file and returns the lines as a list.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..', file_name)
    # print(filename)
    with open(filename, 'r') as assembly_file:
        for line_number ,line in enumerate(assembly_file):
            # removes empty lines and comments
            if (line.isspace()) | (line == '\n') | (line.startswith('#')):
                continue
            line = line.rstrip()
            yield [line_number +1, line]

#Check result of pattern match with line
def pattern_match(line):
    label_re = '((?P<label>\w+): )?'
    label_Declare_re = '(?P<label>\w+) '
    mnemonics_re = '(?P<Mnemonics>\w+)'
    mnemonics_declare_re = '(?P<Mnemonics>D[A-Z]|EQU)'
    operand1_re = '( (?P<Operand1>\w+))?'
    operand2_re = '(, (?P<Operand2>\w+))?'

    pattern1 = label_re + mnemonics_re + operand1_re + operand2_re
    pattern2 = label_Declare_re + mnemonics_declare_re + operand1_re

    pattern_list = [pattern2, pattern1]
    for pattern in pattern_list:
        match = re.match(pattern, line)
        if match:
            return_dict = match.groupdict()
            # for 2nd pattern operand2 is not present so we put none in it
            return_dict['Operand2'] = return_dict.get('Operand2', None)
            return return_dict
    
    return None

def asm_file_field_corrected(line_list : list):
    """
    Corrects the fields of the line in the assembly file.
    """
    asm_line_dict = pattern_match(line_list[1])
    if asm_line_dict is None:
        raise Exception('Error in line {} . Line does not follow correct syntax \
                        . problematic line -\n{}'.format(line_list[0] , line_list[1]))
    
    #checking if no of Mnemonics are correct. IE is 1
    No_of_isMnemonics = sum(mr.isMnemonics(i) for i in asm_line_dict.values())
    if (No_of_isMnemonics == 0):
        raise Exception('Error in line {}. Line does not have Mnemonics'.format(line_list[0]))
    elif(No_of_isMnemonics > 1):
        raise Exception('Error in line {}. Line has more than one Mnemonics'.format(line_list[0]))

    

    #shifting menmonics to the right if label field has Mnemonics
    if(mr.isMnemonics(asm_line_dict['label'])):
        asm_line_dict['Mnemonics'],asm_line_dict['Operand1'], asm_line_dict['Operand2'] = asm_line_dict['label'],asm_line_dict['Mnemonics'],asm_line_dict['Operand1']
    
    return [line_list[0],asm_line_dict]

#output - two dict of 1- extra info and 2- line data
# eg
#[{'line_number': 14}, {'label': None, 'Mnemonics': 'END', 'Operand1': None, 'Operand2': None}]
def final_asm_line_dict(file_name):
    for line_list in assembler_iter(file_name):
        asm_line_dict_list = asm_file_field_corrected(line_list)
        asm_line_dict_list[0] = {'line_number':asm_line_dict_list[0]}
        yield asm_line_dict_list

# #checking asm_file_field_corrected error handling
# print(asm_file_field_corrected([1, 'NEXT: ADD ADD, BREG']))

# for a in mr.Mot_dict():
#     print(a)


# final_asm_line_dict('sampleAssembly.asm') testing
for i in final_asm_line_dict('sampleAssembly.asm'):
    print(i)
    
# # assembler_iter('sampleAssembly.asm') testing
# for i in assembler_iter('sampleAssembly.asm'):
#     print(i)
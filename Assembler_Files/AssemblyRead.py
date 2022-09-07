import os
import re
import Mot_read as mr

registers_name = ['AREG', 'BREG', 'CREG', 'DREG']

# A iterator that returns a line(string) for each line in the file.
# Ignore empty lines and lines starting with a '#'


def assembler_iter(file_name):
    """
    Iterates through the lines of the assembly file and returns the lines as a list.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..', file_name)
    # print(filename)
    with open(filename, 'r') as assembly_file:
        for line in assembly_file:
            # removes empty lines and comments
            if (line.isspace()) | (line == '\n') | (line.startswith('#')):
                continue
            line = line.rstrip()
            yield line


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

# def asm_file_field_corrected(line :str):
#     """
#     Corrects the fields of the line in the assembly file.
#     """
#     # print(line)
#     # print(pattern_match(line))
#     if pattern_match(line) is None:
#         return None
#     else:
#         return_dict = pattern_match(line)
#         # print(return_dict)
#         # print(return_dict['Mnemonics'])
#         # print(mr.isMnemonics(return_dict['Mnemonics']))
#         if mr.isMnemonics(return_dict['Mnemonics']):
#             return return_dict
#         else:
#             return None
    

for a in assembler_iter('sampleAssembly.asm'):
    print(pattern_match(a))



# for a in mr.Mot_dict():
#     print(a)

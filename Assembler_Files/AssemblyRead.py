import os
import re
import Mot_read as mr
import SymbolTableGenration as stg
import LC_Processing as lc

# A iterator that returns [line number , line] for each line in the file.
# Ignore empty lines and lines starting with a '#'
def _assembler_iter(file_name):
    """
    Iterates through the lines of the assembly file and returns the lines as a list.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..', file_name)
    # print(filename)
    with open(filename, 'r') as assembly_file:
        for line_number ,line in enumerate(assembly_file):
            # removes empty lines and comments
            if (line.isspace()) | (line.startswith('#')):
                continue
            # remove comments from line
            if(line.find('#') != -1):
                line = line[:line.find('#')]
            
            line = line.rstrip()
            yield [line_number +1, line]

#Check result of pattern match with line
def _pattern_match(line):
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

def is_constant(operand):
    if(operand.isdigit()):
        return True
    else:
        return False

def is_register(operand):
    if(operand in mr.registers_name):
        return True
    else:
        return False
    
def register_index(register):
    return mr.registers_name.index(register)

def is_BranchCondition(operand):
    if(operand in mr.Branch_condition):
        return True
    else:
        return False
def BranchCondition_index(register):
    return mr.Branch_condition.index(register)
    
    
# takes line_list as input
# returns list of dicts  / dict_list
def _asm_file_field_corrected(line_list : list[int , str]) -> list[dict , dict]:
    """
    Corrects the fields of the line in the assembly file.
    """
    asm_line_dict = _pattern_match(line_list[1])
    if asm_line_dict is None:
        raise Exception('Error in line {} . Line does not follow correct syntax \
                        . problematic line -\n{}'.format(line_list[0] , line_list[1]))
    
    #checking if number of Mnemonics are correct. IE is 1
    No_of_isMnemonics = sum(mr.isMnemonics(i) for i in asm_line_dict.values())
    if (No_of_isMnemonics == 0):
        raise Exception('Error in line {}. Line does not have Mnemonics'.format(line_list[0]))
    elif(No_of_isMnemonics > 1):
        raise Exception('Error in line {}. Line has more than one Mnemonics'.format(line_list[0]))


    #shifting mnemonics to the right if label field has Mnemonics
    if(mr.isMnemonics(asm_line_dict['label'])):
        asm_line_dict['Mnemonics'],asm_line_dict['Operand1'], asm_line_dict['Operand2'] = asm_line_dict['label'],asm_line_dict['Mnemonics'],asm_line_dict['Operand1']
    
    #label Checking
    if (asm_line_dict['label'] is not None and mr.is_word_protected(asm_line_dict['label'] , caseLess=True)):
        raise Exception('Error in line {}. Label {} is a reserved word or similar to it'.format(line_list[0] , asm_line_dict['label']))
    
    
    #Makes dict of extra info like {'line_number': 14}
    properties_dict = {'line_number':line_list[0]}
    asm_line_dict_list = [properties_dict,asm_line_dict]
    
    
    #return Example 
    #[{'line_number': 14}, {'label': None, 'Mnemonics': 'END', 
    # 'Operand1': None, 'Operand2': None}]
    return asm_line_dict_list




# takes filename as input
# returns list of dicts  / dict_list
def line_dict_list_Operand_identified(file_name):
    asm_line_gen = line_dict_list_semi_final(file_name)
    asm_line_gen = lc.LC_processing(asm_line_gen)
    for asm_line_dict_list in asm_line_gen:
        line_dict = asm_line_dict_list[1]
        properties_dict = asm_line_dict_list[0]
        
        #Mnemonics
        MnemonicsIC = '({}, {})'.format(mr.get_Mnemonics_attribute(
            line_dict['Mnemonics'],'Type') , mr.get_Mnemonics_attribute(
            line_dict['Mnemonics'],'Type_id'))
        
        properties_dict['MnemonicsIC']= properties_dict.get('MnemonicsIC', MnemonicsIC)

        #operand check
        for operand_name in ['Operand1' , 'Operand2']:
            operand_name_p = operand_name + 'IC'
            properties_dict[operand_name_p] = properties_dict.get(operand_name_p, '')
            
            if(line_dict[operand_name] is not None):
                if(is_constant(line_dict[operand_name])):
                    properties_dict[operand_name_p] = '(c , {})'.format(line_dict[operand_name])
                elif(is_register(line_dict[operand_name])):
                    properties_dict[operand_name_p] = '(r , {})'.format(str(register_index(line_dict[operand_name])))
                elif(is_BranchCondition(line_dict[operand_name])):
                    properties_dict[operand_name_p] = '(b , {})'.format(str(BranchCondition_index(line_dict[operand_name])))
                #fix it
                else: # it is a symbol
                    Symbol_index = stg.symbol_used(line_dict[operand_name],'Variable' , properties_dict['line_number'])
                    properties_dict[operand_name_p] = '(S , {})'.format(Symbol_index)
            
        # Label check  
        if(line_dict['label'] is not None):
            stg.symbol_defined(line_dict['label'],properties_dict['LC'],'Variable' , properties_dict['line_number'])
        
        asm_line_dict_list=[properties_dict,asm_line_dict_list[1]]
        #return Example
        #[{'line_number': 14,'MnemonicsIC' 'Operand1IC':'(A , 10)',Operand2IC':'(c , 10)'}, {'label': None, 'Mnemonics': 'END',
        yield asm_line_dict_list
         


def line_dict_list_semi_final(file_name):
    for line_list in _assembler_iter(file_name):
        yield _asm_file_field_corrected(line_list)    




#output - two dict of 1- extra info and 2- line data
# eg
#[{'line_number': 14}, {'label': None, 'Mnemonics': 'END', 'Operand1': None, 'Operand2': None}]
def final_asm_line_dict_list(file_name):
    
   return line_dict_list_Operand_identified(file_name)
    
    







# #checking asm_file_field_corrected error handling
# print(asm_file_field_corrected([1, 'NEXT: ADD ADD, BREG']))

# for a in mr.Mot_dict():
#     print(a)


# final_asm_line_dict('sampleAssembly.asm') testing
# for i in final_asm_line_dict('sampleAssembly.asm'):
#     print(i)
    
# # assembler_iter('sampleAssembly.asm') testing
# for i in assembler_iter('sampleAssembly.asm'):
#     print(i)
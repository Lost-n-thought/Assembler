[TOC]



### To Do

- [ ] Make working v1.0

- [ ] execute subroutine from MOT file instead of program files
- [ ] To pass support argument pass for main program (asm = sample.asm and ltorgmode = False)
- [ ] LTORG support
  - [ ] Support Ltorg mode by changing a Variable

- [ ] Check path return by `os.path` module when run inside module
- [x] comment can be at the end of line with statements `Statemnt  #comment123`
- [x] Implement `warning` library instead of print statement
- [ ] `START` and `END` must be only used once
  - [ ] `START` must be first
  - [ ] `END` must be last

- [ ] Uppercase ? How to deal with case?
  - [ ] Mnemonics , Protected Values must be UPPER case .
  - [ ] code can't be similar to them in any case

- [ ] To implement operands checker for each Mnemonics
  - [ ] Implement Protected Symbols(LT LE ET GE GT for jump). Mnemonics are already protected as 
  - [ ] Operand1 and Operand2 in binary (11~2~) = 3 op1 present (10~2~)  both absent(00~2~) = 0

- [ ] Separate leftover LC Processing from assembly file reader
- [x] ~~Learn Hyperlinking within markdown file~~



## <u>Assembler Design</u>

1. It is 2 pass Assembler

   ![Overview of Assembler](./Documents_Files/Overview.png)

   

   

### Program Files

#### 	MOT table reader

1. it reads mot table - which is in file format TSV (tab separated values)

2.  provides functions 

   1. For getting other values from given Mnemonics 

   2. Checking if Mnemonics is valid or not

   3. Return dict with all attributes of given Mnemonics

      ```python
      def get_Mnemonics_attribute(mnemonic :str , attribute = 'Size'):
      def isMnemonics(mnemonic: str):
      def return_given_mnemonics_dict(mnemonic :str):
      ```

3.  

### Pass 1 Files

#### 	Assembly File Reader

1. It reads Assembly (asm) file .
2. True 1 pass reader
   1. It reads by iterator so each line is only read once thought out whole program
3. Supports Comments
   1. Comment line start with "#" .
   2. there can be white space before "#"
   3. removes comment part of line , if it contains both statement and comment
      `Statement #comment`
4. Supports Empty Line
5. Splits the Statement into Label , Mnemonics , Operand1 and Operand2 fields
6. [Error Checks Each line](#Single line Error correction)
7. [Error checks some overall Structure](#Whole ASM program error correction)



#### 	LC Processing

1. Supports `START` and `START 200` like commands
2. Supports `ORG` commands
3. Deals with `DC` and `DS` Statement



#### Symbol Table Generation

##### Protected Words

1. All Mnemonics
2. For Branch condition [LE , LT , ET , GT , GE]
3. Registers Name [AREG, BREG, CREG, DREG]

##### Two Types of Symbol

1. Address Symbols
2. Variable Symbols

##### Symbols Uses Type

1. Declaration
2. Usage

### Pass 2 Files

------



## Assembly Language reference

#### 	Statements

Standard Statements - `Label: Menmonics Operand1, Operand2`

or  `[Label[:] ]Menmonics[ Operand1[, Operand2]]` where `[]` fields are Optional

#### MOT(Mnemonics Opcode Table)

1. Fields of MOT Table are
   1. Mnemonics
   2. Opcode
   3. 



### 	Error Checking

#### 		Whole ASM program error correction

1. `START` must be first command and only used once
2. `END` must be last command and only used once
3. Label
   - [ ] Todo

4. Symbol
   1. 


#### 		Single line Error correction

1. List line No  of the command with error, in Exception reporting




#### line splitting

```
START 200
NEXT: ADD AREG, BREG
SUB AREG, NUMBER
ADD BREG , 5

JUMP NEXT
NUMBER DC 5
CONS1 DC 1
ARRAY DS 10
END
```

#### line format

| Label                                      | Mnemonics   | operand1                                                         | operand2                                   |
| ------------------------------------------ | ----------- | ---------------------------------------------------------------- | ------------------------------------------ |
| [Label[:] ]                                | Mnemonics   | [operand1]                                                       | [, operand2]                               |
| Anylength                                  | max4letters | Anylength                                                        | Anylength                                  |
| Alphanumeric(must start with letter or __) | Aplhabets   | Alphanumeric(must start with letter or __) or number or [symbol] | Alphanumeric(must start with letter or __) |
|                                            |             |                                                                  |                                            |

#### Operation type

1. In all IS staements  only **Operand1** changes **if any**

##### Type - IS 2oprands

eg MOVE A , B

operand1 must be label or Register

​					

| Operrand 1                | Operand 2               |
| ------------------------- | ----------------------- |
| Label(address)or Register | label register constant |


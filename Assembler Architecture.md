[TOC]



### Assembly file Reader

##### Features

1. Supports Comment line
   1. Comment line start with "#" .
   2. thery can be white space before "#"
2. Supports Empty file

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

##### 	Type - IS 2oprands

​		eg MOVE A , B

​			operand1 must be label or Register

​					

| Operrand 1                | Operand 2               |
| ------------------------- | ----------------------- |
| Label(address)or Register | label register constant |

##### 	Type - IS 1 operand

​		INC

​	Type - 

LC processing

 Symbol Table


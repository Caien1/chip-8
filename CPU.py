class CPU:
    def __init__(self):
    
        self.MEMORY :bytearray = bytearray(4096)
        self.REG_SET :dict[str,int] = {"R0" :0x00,
                                    "R1" :0x00,
                                    "R2" :0x00,
                                    "R3" :0x00,
                                    "R4" :0x00,
                                    "R5" :0x00,
                                    "R6" :0x00,
                                    "R7" :0x00,
                                    "R8" :0x00,
                                    "R9" :0x00,
                                    "RA" :0x00,
                                    "RB" :0x00,
                                    "RC" :0x00,
                                    "RD" :0x00,
                                    "RE" :0x00,
                                    "RF" :0x00
                                    }
        self.PC:int = 0X200
        self.STACK :list[int] = [0]*16
        self.SP:int = 0

        self.DELAY_TIMER :int = 0


        self.SOUND_TIMER :int = 0

cpu = CPU()





#fetch
def fetch(address:int,memory:bytearray)->tuple[int,int]:
    opcode_first_byte = memory[address]
    opcode_second_byte = memory[address+1]
    address+=2

    full_opcode = (opcode_first_byte<<8) | opcode_second_byte

    return full_opcode, address


#decode
def decode(opcode:int):
    if opcode == 0x00E0:
        pass
        #cls
    elif opcode == 0x00EE:
        #ret
        pass
    elif (opcode & 0xF000) ==0x1000:

        pass
    elif (opcode & 0xF000) == 0x2000:
        pass
    elif (opcode & 0xF000) == 0x3000:
        pass
    elif (opcode & 0xF000) == 0x4000:
        pass
    elif (opcode & 0xF000) == 0x5000:
        pass
    elif (opcode & 0xF000) == 0x6000:
        pass   
    elif (opcode & 0xF000) == 0x7000:
        pass
    elif (opcode & 0xF000) == 0x8000:
        pass
    elif (opcode & 0xF000) == 0x9000:
        pass
    elif (opcode & 0xF000) == 0xA000:

        pass
    elif (opcode & 0xF000) == 0xA000:

        pass
    elif (opcode & 0xF000) == 0xB000:

        pass
    elif (opcode & 0xF000) == 0xC000:

        pass
    elif (opcode & 0xF000) == 0xD000:

        pass
    elif (opcode & 0xF000) == 0xE000:

        pass
    
    elif (opcode & 0xF000) == 0xF000:

        pass
    else:
        print("No Opcode Find")


#
#









    







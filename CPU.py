class CPU:

    MEMORY :bytearray = bytearray(4096)
    REG_SET :dict[str,bytearray] = {"R0" :bytearray(8),
                                    "R1" :bytearray(8),
                                    "R2" :bytearray(8),
                                    "R3" :bytearray(8),
                                    "R4" :bytearray(8),
                                    "R5" :bytearray(8),
                                    "R6" :bytearray(8),
                                    "R7" :bytearray(8),
                                    "R8" :bytearray(8),
                                    "R9" :bytearray(8),
                                    "RA" :bytearray(8),
                                    "RB" :bytearray(8),
                                    "RC" :bytearray(8),
                                    "RD" :bytearray(8),
                                    "RE" :bytearray(8),
                                    "RF" :bytearray(8)
                                    }
    PC:bytearray = bytearray(16) 
    STACK :list[bytearray] = [bytearray(16) for _ in range(16)]
    SP:bytearray = bytearray(8)

    DELAY_TIMER :bytearray = bytearray(8)


    SOUND_TIMER :bytearray = bytearray(8)



    
    pass

cpu1 = CPU()




print(cpu1.PC[0])



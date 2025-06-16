#memory 4kib 4 * 2^10 bytes = 2^12=>12 bit of address line therfore each word is 8 bits long
# Display  64 * 36 monochrome
# PC program counter
# 16 bit index reg
# 8 bit delay timer ? what is a delay timer? decr 60 times in a second
# 8 bit sound timer beeps if not 0
#VF flag reg -
# 16 -> 8 bit  GP regs named in convenction of hex dec 0 to F
#
#000 -> 1FF first interpreter 0- 511 interpreter location 
#rest from 200 or 512byte is all program?
#DOnt understand the font yet


#IR cycle 
# F -> DCD -> ExE (700 I/s )
# Ins is 2 bytes long => PC = PC + 2
# incr pc as soon as Ins is fetched 
#
# Decode
# DXYN
# INs = 16 bits -> 2 bytes -> 4 nibbles
# FIrst byte:
# first 4 nibble tell you what kind os ins it is 
# X is the 2nd nibble used to identify regs 
# Y third nibble  regs from 0-> from F => GPR
# N 4th nible => 4bit number
#
# Second Byte
#
# DX,NN
# NN (3rd and fourth nibble) 8 bit immidiate number
# 
# D,NNN
# NNN -> 12 bit address


 

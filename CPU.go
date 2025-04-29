package chip8

// designed acc to http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
type CPU struct {
	Memory [4096]byte

	V [16]byte

	I uint16

	//special purpose 8-bit reg delay and Timer
	SD byte
	ST byte

	PC uint16

	SP uint8

	STACK [16]uint16
}

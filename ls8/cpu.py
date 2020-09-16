"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
    
    def ram_read(self, MAR):
        # MAR is Memory Address Register which is the address we want to read
        return self.ram[MAR]
    
    def ram_write(self, MDR, MAR):
        # MDR is Memory Data Register. it contains the data that we are reading or the data that we are going to write
        self.ram[MAR] = MDR
        
    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # storing instruction in variables LDI, PRN, HLT
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        
        # making running state to true to run the program
        running = True

        while running:
            IR = self.ram[self.pc] # Instruction Register, copy of the currently-executing instruction
            
            if IR == HLT:
               running = False
               
            elif IR == LDI:
                # if IR is LDI which is 0b10000010 == 0, then set index number 1
                opperand_a = self.ram[self.pc + 1] # opperand_a == index
                # then set value at index 2
                opperand_b = self.ram[self.pc + 2] # opperand_b == value
                # now register with the given index has the given value
                self.reg[opperand_a] = opperand_b
                print(self.reg)
                # now increment index with 3(coz used 3 bites at three indices) to go to the next instruction
                self.pc += 3 
                
            elif IR == PRN:
                # if the instruction is to print, print the value at +1 index
                opperand_a = self.ram[self.pc + 1]
                print(self.reg[opperand_a])
                # increment the index by 2 to go to the next instruction
                self.pc += 2
                               
            else:
                print(f"unknown instruction {abcd}")
        

"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 # ram = memory
        self.reg = [0] * 8 # reg = registers
        self.pc = 0
        
    
    def ram_read(self, MAR):
        # MAR is Memory Address Register which is the address we want to read
        return self.ram[MAR]
    
    def ram_write(self, MDR, MAR):
        # MDR is Memory Data Register. it contains the data that we are reading or the data that we are going to write
        self.ram[MAR] = MDR
        
    def load(self):
        """Load a program into memory."""

        if len(sys.argv) != 2:
            print(sys.argv)
            print(sys.argv[0])
            print(sys.argv[1])
            print("usage: ls8.py examples/filename")
            sys.exit(1)

        try:
            address = 0

            with open(sys.argv[1]) as f:
                for line in f:
                    t = line.split('#')
                    n = t[0].strip()

                    if n == '':
                        continue

                    try:
                        n = int(n, 2) # for afternoon project we need to (n, base number "2")
                    except ValueError:
                        print(f"Invalid number '{n}'")
                        sys.exit(1)

                    self.ram[address] = n
                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit(2)
        
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MULT":
            self.reg[reg_a]
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

        print(run)

    def run(self):
        """Run the CPU."""
        # storing instruction in variables LDI, PRN, HLT
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        MUL = 0b10100010
        PUSH = 0b01000101
        POP = 0b01000110
        
        SP = 7
        self.reg[SP] = 0xF4
        # making running state to true to run the program
        running = True

        while running:
            IR = self.ram[self.pc] # Instruction Register, copy of the currently-executing instruction
            # setting the index
            opperand_a = self.ram[self.pc + 1] # == index
            # setting the value in the index
            opperand_b = self.ram[self.pc + 2] #  == value for the index
            
            if IR == HLT:
               running = False
               
            elif IR == LDI:
                # if IR is LDI which is 0b10000010 == 0, then set index number 1
                # then set value at index 2
                # now register with the given index has the given value
                self.reg[opperand_a] = opperand_b
                # print(self.reg)
                
                # now increment index with 3(coz used 3 bites at three indices) to go to the next instruction
                self.pc += 3 
                
            elif IR == PRN:
                # if the instruction is to print, print the value at +1 index
                print(self.reg[opperand_a])
                # increment the index by 2 to go to the next instruction
                self.pc += 2
            
            elif IR == MUL:
                product = self.reg[opperand_a] * self.reg[opperand_b]
                # print(self.reg[opperand_a])
                # print(self.reg[opperand_b])
                self.reg[opperand_a] = product
                # print(self.reg[opperand_a])
                # self.ram_write(product, opperand_a)
                self.pc += 3
                print(self.reg)
            
            elif IR == PUSH:
                # Decrement the SP(stack pointer)
                self.reg[SP] -= 1
                # Getting register number to push 
                reg_num = self.ram[self.pc + 1] # is equal to opperand_1
                # Getting the value to push 
                value = self.reg[reg_num]
                #Copying the value to the SP address
                top_of_stack_addr = self.reg[SP]
                self.ram[top_of_stack_addr] = value
                
                self.pc += 2
                # print(self.ram)
                
            elif IR == POP:
                # Getting the register number to pop into
                reg_num = self.ram[self.pc + 1]
                # Getting the top of the stack address
                top_of_stack_addr = self.reg[SP]
                # Getting the value at the top of the stack
                value = self.ram[top_of_stack_addr]
                # Store the value in the register
                self.reg[reg_num] = value
                # incrementing the SP
                self.reg[SP] += 1
                
                self.pc +=2
              
            else:
                print(f"unknown instruction {IR}")
                sys.exit(3)


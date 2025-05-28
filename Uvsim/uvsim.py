import re


class UVSim:
    num_registers = 250

    def __init__(self):
        self.program_counter: int = 0
        self.word_length = 6
        empty_word = '+'+('0'*self.word_length)
        self.accumulator: str = empty_word
        self.memory: list[str] = [empty_word] * UVSim.num_registers


    def _format_value(self, value: int) -> str:
        '''
        Helper function to convert an integer into BasicML word format.
        Ensures the result is a signed, four-digit string.
        '''
        sign = "+" if value >= 0 else "-"
        value = abs(value) % 10**self.word_length

        return f"{sign}{str(value).zfill(self.word_length)}"
    

    def _verify_word(self, word: str) -> int:
        '''
        Verifies the form of BasicML word.
        Returns:
            0: if correctly formed
            -1: if malformed
            -2: if correctly formed except exceeds length
        '''
        re_string = r"[+-]" + r"\d" * self.word_length
        if re.match(re_string, word) is None:
            return -1
        if len(word) > self.word_length + 1:
            return -2
        return 0


    def load_program(self, address: str) -> None:
        program = []

        with open(address, "r") as file:
            program = file.readlines()
        
        # Set simulator's expected word length based on first line of program
        if len(program[0].strip("\n")) < 6:
            self.word_length = 4

        for i in range(len(program)):
            program[i] = program[i].strip("\n")

            if self._verify_word(program[i]) < 0:
                raise ValueError(f"Malformed word on line {i + 1}")

        if len(program) > len(self.memory):
            raise MemoryError("Program exceeds memory!")

        for p in range(len(program)):
            self.memory[p] = program[p]


    def read(self, operand: str, value: int) -> None:
        '''Read a word from the keyboard into a specific location in memory'''

        self.memory[int(operand)] = self._format_value(value)


    def write(self, operand: str) -> str:
        '''Write a word from a specific location in memory to screen'''

        return self.memory[int(operand)]


    def load(self, memoryLocation: str) -> None:
        '''Load a word from a specific location in memory into the accumulator'''

        self.accumulator = self.memory[int(memoryLocation)]


    def store(self, memoryLocation: str) -> None:
        '''Store a word from the accumulator into a specific location in memory'''

        if int(memoryLocation) < 0 or int(memoryLocation) >= len(self.memory):
            raise ValueError("Memory location out of range.")
        
        self.memory[int(memoryLocation)] = self.accumulator


    def add(self, address: str) -> None:
        '''
        Add a word from a specific location in memory to the word in the accumulator
        (leave the result in the accumulator)
        '''

        value = int(self.memory[int(address)])
        accumulator_value = int(self.accumulator)
        accumulator_value += value
        self.accumulator = self._format_value(accumulator_value)


    def subtract(self, address: str) -> None:
        '''
        Subtract a word from a specific location in memory from the word in the accumulator
        (leave the result in the accumulator)
        '''

        value = int(self.memory[int(address)])
        accumulator_value = int(self.accumulator)
        accumulator_value -= value
        self.accumulator = self._format_value(accumulator_value)
    

    def divide(self, address: str) -> None:
        '''
        Divide the word in the accumulator by a word from a specific location in memory
        (leave the result in the accumulator)
        '''

        value = int(self.memory[int(address)])
        accumulator_value = int(self.accumulator)

        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        accumulator_value //= value
        self.accumulator = self._format_value(accumulator_value)


    def multiply(self, address: str) -> None:
        '''
        Multiply a word from a specific location in memory to the word in the accumulator
        (leave the result in the accumulator)
        '''

        value = int(self.memory[int(address)])
        accumulator_value = int(self.accumulator)

        accumulator_value *= value
        self.accumulator = self._format_value(accumulator_value)
    

    def branch(self, operand: str) -> None:
        '''Branch to a specific location in memory'''
        
        self.program_counter = int(operand) - 1


    def branch_neg(self, operand: str) -> None:
        '''Branch to a specific location in memory if the accumulator is negative'''

        # Convert the accumulator from a string to an integer
        accumulator_value = int(self.accumulator)
    
        if accumulator_value < 0:
            self.program_counter = int(operand) - 1


    def branch_zero(self, operand: str) -> None:
        '''Branch to a specific location in memory if the accumulator is zero'''

        accumulator_value = int(self.accumulator)

        if accumulator_value == 0:
            self.program_counter = int(operand) - 1
    

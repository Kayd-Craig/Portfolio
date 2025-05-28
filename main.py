import tkinter as tk

from config import config
from gui import App, event_manager
from uvsim import UVSim


def _get_user_word(uvsim: UVSim, memory_address: str) -> int:
    event_manager.awaiting_input = True

    while True:
        app.write(
            f"Enter the word going into register {memory_address}: ")
        app.root.update()

        while event_manager.awaiting_input:
            app.root.update()

        word = event_manager.gui_input
        app.write(word)  # Echo input back to user

        try:
            int(word)
        except ValueError:
            app.write("Word must be an integer.\n")
            event_manager.awaiting_input = True
            continue

        if uvsim.word_length == 4:
            string_word_length = "four"
        else:
            string_word_length = "six"

        if word[0] in ['+', '-']:
            if len(word[1:]) > uvsim.word_length:
                app.write("Word must be "+string_word_length +
                          " digits or less.\n")
                event_manager.awaiting_input = True
                continue
        elif len(word) > uvsim.word_length:
            app.write("Word must be "+string_word_length+" digits or less.\n")
            event_manager.awaiting_input = True
            continue

        return int(word)


def _end_program():
    while True:
        app.root.update()


def main(program_address: str):

    app.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    app.write(f"Running: {program_address.split('/')[-1]}\n")

    uvsim = UVSim()

    try:
        uvsim.load_program(program_address)
    except ValueError as e:
        app.write(
            f"ERROR! BasicML program could not be loaded: {e}")
        app.write("Exiting program...\n")
        _end_program()
    except MemoryError as e:
        app.write(
            f"WARNING! BasicML program could not be fully loaded: {e}")
        app.write("Continuing execution...\n")
    except FileNotFoundError as e:
        app.write(
            f"ERROR! BasicML program could not be loaded: {e}")
        app.write("Exiting program...\n")
        _end_program()

    while uvsim.program_counter < UVSim.num_registers:
        word = uvsim.memory[uvsim.program_counter]
        mid_point = (len(word) // 2) + 1
        operator = word[1:mid_point]
        operand = word[mid_point:len(word)]

        match int(operator):
            case 10:
                uvsim.read(operand, _get_user_word(uvsim, operand))
            case 11:
                app.write(uvsim.write(operand))
            case 20:
                uvsim.load(operand)
            case 21:
                try:
                    uvsim.store(operand)
                except MemoryError as e:
                    app.write(e)
                    app.write("Continuing execution...\n")
            case 30:
                uvsim.add(operand)
            case 31:
                uvsim.subtract(operand)
            case 32:
                try:
                    uvsim.divide(operand)
                except ZeroDivisionError as e:
                    app.write(e)
                    app.write("Continuing execution...\n")
            case 33:
                uvsim.multiply(operand)
            case 40:
                uvsim.branch(operand)
            case 41:
                uvsim.branch_neg(operand)
            case 42:
                uvsim.branch_zero(operand)
            case 43:
                app.write("Program halted.\n")
                _end_program()
            case _:
                app.write(f'''WARNING! Word on line {
                          uvsim.program_counter} does not have a valid operator''')
                app.write(
                    "Consider putting variable words after the HALT operation")
                app.write("Skipping this line...\n")

        uvsim.program_counter += 1

    app.write("Reached end of program. Terminating...\n")
    _end_program()  # Probably don't actually need to exit


if __name__ == "__main__":
    event_manager.subscribe_run(main)

    global app
    root = tk.Tk()
    app = App(root)
    root.minsize(500, 425)
    root.geometry("500x600")
    root.configure(background=config.primary_color)
    root.mainloop()

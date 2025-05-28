import tkinter as tk
from tkinter import filedialog, scrolledtext

from config import config
from events import EventManager
from file import File
from uvsim import UVSim

event_manager = EventManager()


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("UVSim")
        self.root.protocol("WM_DELETE_WINDOW", root.quit())

        self.files = []

        self.left_frame = tk.Frame(root, bg=config.primary_color)
        self.left_frame.pack(side=tk.LEFT, fill="y", padx=(20, 10), pady=20)

        self.open_frame = tk.Frame(self.left_frame, bg=config.primary_color)
        self.open_frame.pack(fill="x")

        self.open_button = tk.Button(
            self.open_frame,
            text="Open",
            command=self.open_file,
            bg=config.secondary_color,
            highlightbackground=config.primary_color
        )
        self.open_button.pack(side=tk.LEFT)

        self.file_listbox = tk.Listbox(self.left_frame)
        self.file_listbox.pack(fill="both", expand=True, pady=10)
        self.file_listbox.bind("<<ListboxSelect>>", self.file_selected)

        self.button_frame = tk.Frame(self.left_frame, bg=config.primary_color)
        self.button_frame.pack(fill="x")

        self.save_button = tk.Button(
            self.button_frame,
            text="Save",
            command=self.save_file,
            bg=config.secondary_color,
            highlightbackground=config.primary_color
        )
        self.save_button.pack(side=tk.LEFT)

        self.save_as_button = tk.Button(
            self.button_frame,
            text="Save As",
            command=self.save_file_as,
            bg=config.secondary_color,
            highlightbackground=config.primary_color
        )
        self.save_as_button.pack(side=tk.LEFT, padx=10)

        self.run_button = tk.Button(
            self.button_frame,
            text="Run",
            command=self.run,
            bg=config.secondary_color,
            highlightbackground=config.primary_color
        )
        self.run_button.pack(side=tk.LEFT)

        self.right_frame = tk.Frame(root, bg=config.primary_color)
        self.right_frame.pack(side=tk.LEFT, fill="both",
                              expand=True, padx=(10, 20), pady=20)

        self.editor = scrolledtext.ScrolledText(
            self.right_frame,
            wrap=tk.WORD,
            height=10,
            width=10
        )
        self.editor.pack(fill="both", expand=True)
        self.editor.bind("<KeyRelease>", self.limit_and_save_contents)

        self.console_frame = tk.Frame(
            self.right_frame, bg=config.primary_color)
        self.console_frame.pack(fill="x")

        self.console = scrolledtext.ScrolledText(
            self.console_frame,
            wrap=tk.WORD,
            height=10,
            width=10,
            state=tk.DISABLED
        )
        self.console.pack(fill="x", pady=(20, 10))

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.console_frame,
            textvariable=self.input_var,
            width=7
        )
        self.input_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=25)
        self.input_entry.bind("<Return>", self.send_input)

        self.send_button = tk.Button(
            self.console_frame,
            text="Enter",
            command=self.send_input,
            bg=config.secondary_color,
            highlightbackground=config.primary_color
        )
        self.send_button.pack(side=tk.RIGHT)

    def write(self, text: str) -> None:
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text + "\n")
        self.console.config(state=tk.DISABLED)
        self.console.see(tk.END)

    def send_input(self, event=None) -> None:
        input_text = self.input_var.get()
        self.input_var.set("")
        event_manager.publish_enter(input_text)

    def add_file(self, file: File) -> None:
        self.files.append(file)
        self.file_listbox.insert(tk.END, file.name)
        self.file_listbox.selection_clear(0, tk.END)
        self.file_listbox.selection_set(tk.END)

    def current_file_index(self) -> int:
        return self.file_listbox.curselection()[0]

    def current_file(self) -> File:
        index = self.current_file_index()
        return self.files[index]

    def limit_and_save_contents(self, event) -> None:
        num_lines = int(self.editor.index("end-1c").split(".")[0])
        if num_lines > UVSim.num_registers:
            self.editor.delete(str(float(UVSim.num_registers + 1)), tk.END)

        if len(self.files) > 0:
            file = self.current_file()
            file.contents = self.editor.get(1.0, tk.END)

    def fill_editor(self) -> None:
        file = self.current_file()
        self.editor.delete(1.0, tk.END)
        self.editor.insert(tk.END, file.contents)

    def file_selected(self, event) -> None:
        self.fill_editor()

    def open_file(self) -> None:
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        file = File(file_path)

        self.add_file(file)
        self.fill_editor()

    def save_file_as(self) -> None:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return

        contents = self.editor.get(1.0, tk.END)

        file = File(file_path, contents)
        file.save_file()
        self.add_file(file)

    def save_file(self) -> None:
        if len(self.files) == 0:
            return self.save_file_as()

        file = self.current_file()
        file.save_file()

    def run(self) -> None:
        if len(self.files) == 0:
            return self.save_file_as()

        file = self.current_file()
        event_manager.publish_run(file.path)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

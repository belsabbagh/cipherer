import tkinter as tk
from tkinter import ttk

STD_PACK = {"padx": 5, "pady": 5, "expand": True}


class FileButtons(tk.Frame):
    frame = None
    openButton = None
    saveButton = None

    def __init__(self, master, commands) -> None:
        self.openButton = ttk.Button(master, text="Open", command=commands["open"])
        self.saveButton = ttk.Button(master, text="Save", command=commands["save"])
        self.openButton.pack(side=tk.LEFT, padx=5, pady=5)
        self.saveButton.pack(side=tk.LEFT, padx=5, pady=5)


class TextEndpoint:
    textArea = None
    fileButtons = None
    label = None
    fileButtonsFrame = None

    def __init__(self, master, name, button_commands):
        self.textArea = tk.Text(master, width=40, height=20)
        self.label = ttk.Label(master, text=name)
        self.fileButtonsFrame = tk.Frame(master)
        self.fileButtons = FileButtons(self.fileButtonsFrame, button_commands)
        self.label.pack(side=tk.TOP)
        self.textArea.pack(side=tk.TOP)
        self.fileButtonsFrame.pack(side=tk.TOP)


class Controls:
    encMethod = None
    keyTextArea = None
    vigenereMode = None
    encryptButton = None
    decryptButton = None

    def __init__(self, master, enc_cmd, dec_cmd) -> None:
        self.encMethod = LabeledDropdown()
        self.keyTextArea = tk.Text(master, width=7, height=7)
        self.vigenereMode
        encryptButton = ttk.Button(master, text="Encrypt", command=enc_cmd)
        decryptButton = ttk.Button(master, text="Decrypt", command=dec_cmd)


class LabeledDropdown:
    label = None
    dropdown = None

    def __init__(self, master, label, options, callback=None) -> None:
        self.label = tk.Label(master, text=label)
        self.dropdown = tk.OptionMenu(
            master,
            tk.StringVar(),
            *options,
            command=callback,
        )
        self.label.pack(side=tk.LEFT, **STD_PACK)
        self.dropdown.pack(side=tk.LEFT, **STD_PACK)

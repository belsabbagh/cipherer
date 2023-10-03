import tkinter as tk


class FileButtons(tk.Frame):
    frame = None
    openButton = None
    saveButton = None

    def __init__(self, master, commands) -> None:
        self.openButton = tk.Button(master, text="Open", command=commands["open"])
        self.saveButton = tk.Button(master, text="Save", command=commands["save"])
        self.openButton.pack(side=tk.LEFT)
        self.saveButton.pack(side=tk.LEFT)


class TextEndpoint:
    textArea = None
    fileButtons = None
    label = None
    fileButtonsFrame = None

    def __init__(self, master, name, button_commands):
        self.textArea = tk.Text(master, width=40, height=20)
        self.label = tk.Label(master, text=name)
        self.fileButtonsFrame = tk.Frame(master)
        self.fileButtons = FileButtons(self.fileButtonsFrame, button_commands)
        self.label.pack(side=tk.TOP)
        self.textArea.pack(side=tk.TOP)
        self.fileButtonsFrame.pack(side=tk.TOP)
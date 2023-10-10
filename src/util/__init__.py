
import tkinter as tk
import tkinter.filedialog as fd
from src.gui.state import state


def clean_text(text):
    return "".join(c for c in text if c.isalpha()).upper()



def writeTextArea(textArea, text):
    textArea.delete("1.0", tk.END)
    textArea.insert("1.0", text)


def openToText(output):
    filename = fd.askopenfilename()
    with open(filename, "r") as file:
        plainText = file.read()
    writeTextArea(output, plainText)


def saveFromText(textArea, name):
    filename = fd.asksaveasfile(
        initialfile=f"{name}.txt",
        mode="w",
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")],
    )
    if filename is None:
        return
    text = textArea.get("1.0", tk.END)
    filename.write(text)
    filename.close()

import tkinter as tk
from src.methods import *
import tkinter.filedialog as fd

ENC_MODES = {
    "Caesar": Caesar,
    "Playfair": Playfair,
    "Hill": Hill,
    "Vigenere": Vigenere,
    "Vernam": Vernam,
}
STD_PACK = {"padx": 5, "pady": 5, "expand": True}


def clean_text(text):
    return "".join([c for c in text if c.isalpha()]).upper()


def get_state():
    encMethod = dropDown.cget("text")
    key = keyTextArea.get("1.0", tk.END).rsplit("\n", 1)[0]
    if encMethod != "Hill":
        key = key.replace("\n", "")
    state = {
        "plainText": clean_text(plainTextArea.get("1.0", tk.END)),
        "cipherText": clean_text(cipherTextArea.get("1.0", tk.END)),
        "encMethod": encMethod,
        "key": key,
    }
    print(state)
    return state


def writeTextArea(textArea, text):
    textArea.delete("1.0", tk.END)
    textArea.insert("1.0", text)


def encrypt():
    state = get_state()
    try:
        encMethod = ENC_MODES[state["encMethod"]](state["key"])
        cipherText = encMethod.encrypt(state["plainText"])
        writeTextArea(cipherTextArea, cipherText)
        del encMethod
    except Exception as e:
        tk.messagebox.showerror("Error", e)


def decrypt():
    state = get_state()
    cipherText = state["cipherText"]
    encMethod = ENC_MODES[state["encMethod"]](state["key"])

    plainText = encMethod.decrypt(cipherText)
    writeTextArea(plainTextArea, plainText)
    del encMethod


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


file_commands = {
    "encrypt": {
        "open": lambda: openToText(plainTextArea),
        "save": lambda: saveFromText(plainTextArea, "plaintext"),
    },
    "decrypt": {
        "open": lambda: openToText(cipherTextArea),
        "save": lambda: saveFromText(cipherTextArea, "ciphertext"),
    },
}


def fileButtons(master, commands):
    frame = tk.Frame(master)
    openButton = tk.Button(frame, text="Open", command=commands["open"])
    saveButton = tk.Button(frame, text="Save", command=commands["save"])
    openButton.pack(side=tk.LEFT, **STD_PACK)
    saveButton.pack(side=tk.LEFT, **STD_PACK)
    return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cipherer")
    root.geometry("840x600")
    root.minsize(840, 640)
    row = tk.Frame(root)
    row.pack(side=tk.TOP, fill=tk.BOTH, **STD_PACK)

    textAreaFrame = tk.Frame(row)
    textAreaFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    textAreaLabel = tk.Label(textAreaFrame, text="Plain Text")
    textAreaLabel.pack(side=tk.TOP, **STD_PACK)
    plainTextArea = tk.Text(textAreaFrame, width=40, height=20)
    plainTextArea.pack(side=tk.TOP, **STD_PACK)
    fileButtons(textAreaFrame, file_commands["encrypt"]).pack(side=tk.TOP, **STD_PACK)

    buttonFrame = tk.Frame(row)
    buttonFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    dropDown = tk.OptionMenu(
        buttonFrame,
        tk.StringVar(),
        *list(ENC_MODES.keys()),
    )
    dropDown.pack(side=tk.TOP, **STD_PACK)
    keyTextArea = tk.Text(buttonFrame, width=7, height=7)
    keyTextArea.pack(side=tk.TOP, **STD_PACK)
    encryptButton = tk.Button(buttonFrame, text="Encrypt", command=encrypt)
    encryptButton.pack(side=tk.TOP, **STD_PACK)
    decryptButton = tk.Button(buttonFrame, text="Decrypt", command=decrypt)
    decryptButton.pack(side=tk.TOP, **STD_PACK)

    textAreaFrame = tk.Frame(row)
    textAreaFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    textAreaLabel = tk.Label(textAreaFrame, text="Cipher Text")
    textAreaLabel.pack(side=tk.TOP, **STD_PACK)
    cipherTextArea = tk.Text(textAreaFrame, width=40, height=20)
    cipherTextArea.pack(side=tk.TOP, **STD_PACK)
    fileButtons(textAreaFrame, file_commands["decrypt"]).pack(side=tk.TOP, **STD_PACK)

    root.mainloop()

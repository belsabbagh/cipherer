import tkinter as tk
from src.methods import *

ENC_MODES = {
    "Caesar": Caesar,
    "Playfair": Playfair,
    "Hill": Hill,
    "Vigenere": Vigenere,
    "Vernam": Vernam,
}
STD_PACK = {"padx": 5, "pady": 5, "expand": True}


def get_state():
    encMethod = dropDown.cget("text")
    key = keyTextArea.get("1.0", tk.END).rsplit("\n", 1)[0]
    if encMethod != "Hill":
        key = key.replace("\n", "")
    state = {
        "plainText": plainTextArea.get("1.0", tk.END).replace("\n", ""),
        "cipherText": cipherTextArea.get("1.0", tk.END).replace("\n", ""),
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
    encMethod = ENC_MODES[state["encMethod"]](state["key"])
    cipherText = encMethod.encrypt(state["plainText"])
    writeTextArea(cipherTextArea, cipherText)


def decrypt():
    state = get_state()
    cipherText = state["cipherText"]
    encMethod = ENC_MODES[state["encMethod"]](state["key"])

    plainText = encMethod.decrypt(cipherText)
    writeTextArea(plainTextArea, plainText)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cipherer")
    root.geometry("840x640")
    root.minsize(840, 640)
    row = tk.Frame(root)
    row.pack(side=tk.LEFT, fill=tk.BOTH, **STD_PACK)

    textAreaFrame = tk.Frame(row)
    textAreaFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    textAreaLabel = tk.Label(textAreaFrame, text="Plain Text")
    textAreaLabel.pack(side=tk.TOP, **STD_PACK)
    plainTextArea = tk.Text(textAreaFrame, width=40, height=20)
    plainTextArea.pack(side=tk.TOP, **STD_PACK)

    buttonFrame = tk.Frame(row)
    buttonFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    dropDown = tk.OptionMenu(
        buttonFrame,
        tk.StringVar(),
        *list(ENC_MODES.keys()),
    )
    dropDown.pack(side=tk.TOP, **STD_PACK)
    keyTextArea = tk.Text(buttonFrame, width=7, height=5)
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

    root.mainloop()

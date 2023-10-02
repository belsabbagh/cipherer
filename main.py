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
    plainText = plainTextArea.get("1.0", tk.END).replace("\n", "")
    cipherText = cipherTextArea.get("1.0", tk.END).replace("\n", "")
    encMethod = dropDown.cget("text")
    key = keyTextArea.get("1.0", tk.END).rsplit('\n', 1)[0]
    if encMethod != "Hill":
        key = key.replace("\n", "")
    state = {
        "plainText": plainText,
        "cipherText": cipherText,
        "encMethod": dropDown.cget("text"),
        "key": key,
    }
    print(state)
    return state


def writeTextArea(textArea, text):
    textArea.delete("1.0", tk.END)
    textArea.insert("1.0", text)


def encrypt():
    state = get_state()
    plainText = state["plainText"]
    encMethod = ENC_MODES[state["encMethod"]](state["key"])

    cipherText = encMethod.encrypt(plainText)
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
    root.geometry("1024x720")

    row = tk.Frame(root)
    row.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)

    buttonFrame = tk.Frame(root)
    buttonFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)

    cipherTextArea = tk.Text(root, width=40, height=20)
    cipherTextArea.pack(side=tk.LEFT, **STD_PACK)

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

    plainTextArea = tk.Text(row, width=40, height=20)
    plainTextArea.pack(side=tk.LEFT, **STD_PACK)

    root.mainloop()

import tkinter as tk
from tkinter import ttk
from cryptexia.cryptexia.ciphers.classic import Caesar, Playfair, Hill, Vigenere
from src.gui.state import state
from src import util
from src.gui import TextEndpoint, STD_PACK, LabeledDropdown


ENC_MODES = {
    "Caesar": Caesar,
    "Playfair": Playfair,
    "Hill": Hill,
    "Vigenere": Vigenere,
}

hints = {
    "Caesar": "Enter a value between 0 and 26 to encrypt/decrypt.",
    "Playfair": "Enter a keyword to construct the playfair matrix.",
    "Hill": "Enter an invertible square matrix (in CSV format) to construct the key.",
    "Vigenere": "Enter a keyword to construct the key. Choose a mode (auto, repeat) to build the key.",
}


file_commands = {
    "encrypt": {
        "open": lambda: util.openToText(plainTextEndpoint.textArea),
        "save": lambda: util.saveFromText(plainTextEndpoint.textArea, "plaintext"),
    },
    "decrypt": {
        "open": lambda: util.openToText(cipherTextEndpoint.textArea),
        "save": lambda: util.saveFromText(cipherTextEndpoint.textArea, "ciphertext"),
    },
}


def update_state():
    encMethod = encMethodComponent.dropdown.cget("text")
    key = keyTextArea.get("1.0", tk.END).rsplit("\n", 1)[0]
    if encMethod != "Hill":
        key = key.replace("\n", "")
    state["key"] = key
    state["plainText"] = util.clean_text(plainTextEndpoint.textArea.get("1.0", tk.END))
    state["cipherText"] = util.clean_text(
        cipherTextEndpoint.textArea.get("1.0", tk.END)
    )
    state["vigenereMode"] = vigenereMode.dropdown.cget("text")
    return state


def show_selected(value):
    state["encMethod"] = value
    hint_text.set(hints.get(value, ""))


def encrypt():
    state = update_state()
    try:
        args = [state["key"]]
        if state["encMethod"] == "Vigenere":
            args.append(state["vigenereMode"].lower())
        encMethod = ENC_MODES[state["encMethod"]](*args)
        cipherText = encMethod.encrypt(state["plainText"])
        util.writeTextArea(cipherTextEndpoint.textArea, cipherText)
        del encMethod
    except Exception as e:
        tk.messagebox.showerror("Error", e)


def decrypt():
    state = update_state()
    try:
        encMethod = ENC_MODES[state["encMethod"]](state["key"])
        plainText = encMethod.decrypt(state["cipherText"])
        util.writeTextArea(plainTextEndpoint.textArea, plainText)
        del encMethod
    except Exception as e:
        tk.messagebox.showerror("Error", e)


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("winnative")
    root.title("Cipherer")
    root.geometry("1200x600")
    root.minsize(840, 600)

    hint_text = tk.StringVar()
    hint_text.set("")

    row = tk.Frame(root)
    hint = tk.Label(root, textvariable=hint_text)
    hint.pack(side=tk.TOP, fill=tk.BOTH, pady=4)
    row.pack(side=tk.TOP, fill=tk.BOTH, **STD_PACK)

    plainTextFrame = tk.Frame(row)
    controlsFrame = tk.Frame(row)
    cipherTextFrame = tk.Frame(row)
    plainTextFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    controlsFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)
    cipherTextFrame.pack(side=tk.LEFT, fill=tk.X, **STD_PACK)

    plainTextEndpoint = TextEndpoint(
        plainTextFrame, "Plaintext", file_commands["encrypt"]
    )

    encMethodFrame = tk.Frame(controlsFrame)
    encMethodComponent = LabeledDropdown(
        encMethodFrame, "Encryption Method", list(ENC_MODES.keys()), show_selected
    )

    keyTextArea = tk.Text(controlsFrame, width=7, height=7)
    vigenereModeFrame = tk.Frame(controlsFrame)
    encryptButton = ttk.Button(controlsFrame, text="Encrypt", command=encrypt)
    decryptButton = ttk.Button(controlsFrame, text="Decrypt", command=decrypt)

    encMethodFrame.pack(side=tk.TOP, **STD_PACK)
    keyTextArea.pack(side=tk.TOP, **STD_PACK)
    vigenereModeFrame.pack(side=tk.TOP, **STD_PACK)
    encryptButton.pack(side=tk.TOP, **STD_PACK)
    decryptButton.pack(side=tk.TOP, **STD_PACK)

    vigenereMode = LabeledDropdown(
        vigenereModeFrame, "Vigenere Mode", ["Auto", "Repeat"]
    )
    cipherTextEndpoint = TextEndpoint(
        cipherTextFrame, "Ciphertext", file_commands["decrypt"]
    )

    root.mainloop()

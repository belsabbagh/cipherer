from PyQt6 import QtWidgets as QtW
from src.gui.endpoint import TextEndpoint
from cryptexia.cryptexia.ciphers.classic import Caesar, Playfair, Hill, Vigenere, Vernam
from src.util import openToText, saveFromText


ciphers = {
    "Caesar": Caesar,
    "Playfair": Playfair,
    "Hill": Hill,
    "Vigenere": Vigenere,
    "Vernam": Vernam,
}

file_cmds = {
    "plain": {
        "open": lambda x: openToText(x),
        "save": lambda x: saveFromText(x, "plain.txt"),
    },
    "cipher": {
        "open": lambda x: openToText(x),
        "save": lambda x: saveFromText(x, "cipher.txt"),
    },
}


class MainWindow(QtW.QMainWindow):
    plainEndpoint = None
    cipherEndpoint = None
    controls = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(1000, 600)
        mainWidget = QtW.QGroupBox()
        mainLayout = QtW.QHBoxLayout()
        self.plainEndpoint = TextEndpoint("Plain Text", file_cmds["plain"])
        self.cipherEndpoint = TextEndpoint("Cipher Text", file_cmds["cipher"])
        self.controls = Controls(
            {"encrypt": self.on_encrypt, "decrypt": self.on_decrypt}
        )
        mainLayout.addWidget(self.plainEndpoint)
        mainLayout.addWidget(self.controls)
        mainLayout.addWidget(self.cipherEndpoint)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def __process(self, inTextEdit, outTextEdit, run_fn):
        key = self.controls.keyTextArea.toPlainText()
        method = self.controls.encMethod.currentText()
        args = [key]
        if method == "Vigenere":
            args.append(self.controls.vigenereMode.currentText())
        cipher = ciphers[method](*args)
        text = inTextEdit.toPlainText().strip().upper().replace(" ", "")
        outTextEdit.setText(run_fn(cipher, text))

    def on_encrypt(self):
        run_fn = lambda cipher, text: cipher.encrypt(text)
        try:
            self.__process(
                self.plainEndpoint.textArea, self.cipherEndpoint.textArea, run_fn
            )
        except Exception as e:
            QtW.QMessageBox.critical(self, "Error", str(e))

    def on_decrypt(self):
        run_fn = lambda cipher, text: cipher.decrypt(text)
        try:
            self.__process(
                self.plainEndpoint.textArea, self.cipherEndpoint.textArea, run_fn
            )
        except Exception as e:
            QtW.QMessageBox.critical(self, "Error", str(e))


class Controls(QtW.QWidget):
    encMethod = None
    keyTextArea = None
    vigenereMode = None
    encryptButton = None
    decryptButton = None

    def __init__(self, button_commands):
        super().__init__()
        self.layout = QtW.QVBoxLayout()
        self.encMethod = QtW.QComboBox()
        self.encMethod.addItems(list(ciphers.keys()))
        self.keyTextArea = QtW.QTextEdit()
        self.keyTextArea.resize(100, 100)
        self.vigenereMode = QtW.QComboBox()
        self.vigenereMode.addItems(["Auto", "Repeat"])
        self.encryptButton = QtW.QPushButton(
            "Encrypt", clicked=button_commands["encrypt"]
        )
        self.decryptButton = QtW.QPushButton(
            "Decrypt", clicked=button_commands["decrypt"]
        )
        self.layout.addWidget(self.encMethod)
        self.layout.addWidget(self.keyTextArea)
        self.layout.addWidget(self.vigenereMode)
        self.layout.addWidget(self.encryptButton)
        self.layout.addWidget(self.decryptButton)
        self.setLayout(self.layout)

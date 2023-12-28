from PyQt6 import QtWidgets as QtW
from src.gui.endpoint import TextEndpoint
from src.gui.controls import Controls
from src.util import openToText, saveFromText
from src.config import CIPHERS

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
    plainEndpoint: TextEndpoint
    cipherEndpoint: TextEndpoint
    controls: Controls
    cipher: dict

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
            args.append(self.controls.vigenereMode.currentText().lower())
        cipher = CIPHERS[method]
        c = cipher["class"](*args)
        h = cipher["hint"]
        self.controls.hint.setText(h)
        text = inTextEdit.toPlainText().strip().upper().replace(" ", "")
        outTextEdit.setText(run_fn(c, text))

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
                self.cipherEndpoint.textArea, self.plainEndpoint.textArea, run_fn
            )
        except Exception as e:
            QtW.QMessageBox.critical(self, "Error", str(e))

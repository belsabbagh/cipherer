from PyQt6 import QtWidgets as QtW
from src.config import CIPHERS

class Controls(QtW.QWidget):
    hint: QtW.QLabel
    encMethod: QtW.QComboBox
    keyTextArea: QtW.QTextEdit
    vigenereMode: QtW.QComboBox
    encryptButton: QtW.QPushButton
    decryptButton: QtW.QPushButton

    def __init__(self, button_commands):
        super().__init__()
        ciphers = list(CIPHERS.keys())
        self.layout = QtW.QVBoxLayout()  # type: ignore
        self.encMethod = QtW.QComboBox()
        self.encMethod.addItems(ciphers)
        self.encMethod.currentTextChanged.connect(self.on_combobox_changed)
        self.keyTextArea = QtW.QTextEdit()
        self.keyTextArea.resize(100, 100)
        self.vigenereMode = QtW.QComboBox()
        self.vigenereMode.addItems(["Auto", "Repeat"])
        self.encryptButton = QtW.QPushButton("Encrypt")
        self.encryptButton.clicked.connect(button_commands["encrypt"])
        self.decryptButton = QtW.QPushButton("Decrypt")
        self.decryptButton.clicked.connect(button_commands["decrypt"])
        self.hint = QtW.QLabel()
        self.hint.setText(CIPHERS[ciphers[0]]["hint"])
        self.layout.addWidget(self.hint)
        self.layout.addWidget(self.encMethod)
        self.layout.addWidget(self.keyTextArea)
        self.layout.addWidget(self.vigenereMode)
        self.layout.addWidget(self.encryptButton)
        self.layout.addWidget(self.decryptButton)
        self.setLayout(self.layout)

    def on_combobox_changed(self, text):
        parent: MainWindow = self.parent()  # type: ignore
        parent.cipher = CIPHERS[text]
        self.hint.setText(parent.cipher["hint"])

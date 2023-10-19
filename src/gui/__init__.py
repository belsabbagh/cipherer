from PyQt6 import QtWidgets as QtW
import PyQt6 as Qt
from cryptexia.cryptexia.ciphers.classic import Caesar, Playfair, Hill, Vigenere, Vernam
from src.util import openToText, saveFromText

file_cmds = {
    "plain": {
        "open": lambda x: openToText(x),
        "save": lambda x: saveFromText(x, "plain.txt"),
    },
    "cipher": {
        "open": lambda x: openToText(x),
        "save": lambda x: saveFromText(x, "cipher.txt")
    },
}

ciphers = {
    "Caesar": Caesar,
    "Playfair": Playfair,
    "Hill": Hill,
    "Vigenere": Vigenere,
    "Vernam": Vernam,
}


class App(QtW.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MainWindow()
        self.window.show()


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
        self.controls = Controls({"encrypt": self.on_encrypt, "decrypt": self.on_decrypt})
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
        self.__process(self.plainEndpoint.textArea, self.cipherEndpoint.textArea, run_fn)

    def on_decrypt(self):
        run_fn = lambda cipher, text: cipher.decrypt(text)
        self.__process(self.cipherEndpoint.textArea, self.plainEndpoint.textArea, run_fn)


class TextEndpoint(QtW.QWidget):
    textArea = None
    label = None
    layout = None
    fileButtons = None

    def __init__(self, name, button_commands):
        super().__init__()
        self.button_commands = button_commands
        self.textArea = QtW.QTextEdit()
        self.label = QtW.QLabel(name)
        self.label.setAlignment(Qt.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout = QtW.QVBoxLayout()
        self.fileButtons = FileButtons({ "open": self.on_open, "save": self.on_save})
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.fileButtons)
        self.setLayout(self.layout)
        
    def on_open(self):
        self.button_commands["open"](self.textArea)
    
    def on_save(self):
        self.button_commands["save"](self.textArea)

    def write(self, text):
        self.textArea.setText(text)
        
    def read(self):
        return self.textArea.toPlainText()


class FileButtons(QtW.QWidget):
    def __init__(self, commands):
        super().__init__()
        self.openButton = Qt.QtWidgets.QPushButton("Open", clicked=commands["open"])
        self.saveButton = Qt.QtWidgets.QPushButton("Save", clicked=commands["save"])
        self.layout = QtW.QHBoxLayout()
        self.layout.addWidget(self.openButton)
        self.layout.addWidget(self.saveButton)
        self.setLayout(self.layout)


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
        self.encryptButton = QtW.QPushButton("Encrypt", clicked=button_commands["encrypt"])
        self.decryptButton = QtW.QPushButton("Decrypt", clicked=button_commands["decrypt"])
        self.layout.addWidget(self.encMethod)
        self.layout.addWidget(self.keyTextArea)
        self.layout.addWidget(self.vigenereMode)
        self.layout.addWidget(self.encryptButton)
        self.layout.addWidget(self.decryptButton)
        self.setLayout(self.layout)

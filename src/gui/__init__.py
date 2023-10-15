from PyQt6 import QtWidgets as QtW
import PyQt6 as Qt


class App(QtW.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MainWindow()
        self.window.show()


class MainWindow(QtW.QMainWindow):
    plainTextEndpoint = None
    cipherTextEndpoint = None
    controls = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(1000, 600)
        mainWidget = QtW.QGroupBox()
        mainLayout = QtW.QHBoxLayout()
        self.plainTextEndpoint = TextEndpoint(
            "Plain Text", {"open": lambda x: x, "save": lambda x: x}
        )
        self.cipherTextEndpoint = TextEndpoint(
            "Cipher Text", {"open": lambda x: x, "save": lambda x: x}
        )
        self.controls = Controls()
        mainLayout.addWidget(self.plainTextEndpoint)
        mainLayout.addWidget(self.controls)
        mainLayout.addWidget(self.cipherTextEndpoint)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)


class TextEndpoint(QtW.QWidget):
    textArea = None
    label = None
    layout = None
    fileButtons = None

    def __init__(self, name, button_commands):
        super().__init__()
        self.textArea = QtW.QTextEdit()
        self.label = QtW.QLabel(name)
        self.label.setAlignment(Qt.QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout = QtW.QVBoxLayout()
        self.fileButtons = FileButtons(button_commands)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.fileButtons)
        self.setLayout(self.layout)

    def write(self, text):
        self.textArea.setText(text)


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

    def __init__(self):
        super().__init__()
        self.layout = QtW.QVBoxLayout()
        self.encMethod = QtW.QComboBox()
        self.encMethod.addItems(["Caesar", "Vigenere", "Hill"])
        self.keyTextArea = QtW.QTextEdit()
        self.keyTextArea.resize(100, 100)
        self.vigenereMode = QtW.QComboBox()
        self.vigenereMode.addItems(["Auto", "Repeat"])
        self.encryptButton = QtW.QPushButton("Encrypt")
        self.decryptButton = QtW.QPushButton("Decrypt")
        self.layout.addWidget(self.encMethod)
        self.layout.addWidget(self.keyTextArea)
        self.layout.addWidget(self.vigenereMode)
        self.layout.addWidget(self.encryptButton)
        self.layout.addWidget(self.decryptButton)
        self.setLayout(self.layout)

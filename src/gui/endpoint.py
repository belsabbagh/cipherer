from PyQt6 import QtWidgets as QtW
import PyQt6 as Qt

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

from PyQt6 import QtWidgets as QtW

def clean_text(text):
    return "".join(c for c in text if c.isalpha()).upper()



def writeTextArea(textArea: QtW.QTextEdit, text):
    textArea.setText(text)


def openToText(output):
    filename, _ = QtW.QFileDialog.getOpenFileName(
        None,
        "Open File",
        "",
        "Text Files (*.txt);;All Files (*)",
    )
    if not filename:
        return
    with open(filename, "r") as f:
        plainText = f.read()
    writeTextArea(output, plainText)

def saveFromText(textArea: QtW.QTextEdit, name):
    filename, _ = QtW.QFileDialog.getSaveFileName(
        None,
        "Save File",
        name,
        "Text Files (*.txt);;All Files (*)",
    )
    if not filename:
        return
    with open(filename, "w") as f:
        f.write(textArea.toPlainText())


# Cipherer

Cipherer is a Python program that demonstrates five famous and traditional encryption techniques: Caesar, Playfair, Hill, Vigenere, and Vernam. Each encryption method offers a unique approach to securing information through mathematical transformations and substitution. This project was built in partial fulfillment of our network security course.

## Run Project

Clone the project

```bash
  git clone https://github.com/belsabbagh/cipherer.git
```

Go to the project directory

```bash
  cd cipherer
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```

## Build

To build this project run

```bash
   python -m PyInstaller --onefile --noconfirm --name=cipherer  main.py 
```

The `cipher.exe` file can be found in `./dist`

## Usage

The app window is divided into 3 vertical sections:

\begin{itemize}
\item The left section is the input area where the user can enter the plaintext.
\item The middle section is the control area where the user can select the encryption method and enter the encryption key.
\item The right section is the output area where the user can see the encrypted text and enter encrypted text to decrypt.
\end{itemize}

In the plaintext or ciphertext input area, the user can enter the text to be encrypted or decrypted. The user can also copy and paste text from other sources or open text files to be encrypted or decrypted.

In the control area, the user can select the encryption method from the dropdown menu. The user can also enter the encryption key.

\begin{itemize}
\item For the Caesar cipher, the key is the number of shifts.
\item For the Playfair cipher, the key is the keyword.
\item For the Hill cipher, the key is a square matrix in CSV format.
\item For the Vigenere cipher, the key is the keyword.
\item For the Vernam cipher, the key is the keyword.
\end{itemize}

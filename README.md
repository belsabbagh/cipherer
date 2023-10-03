
# Cipherer

Cipherer is a demo for classic cipher methods built in partial fulfillment of my network security course.

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
   python -m PyInstaller --onefile --noconfirm --name=cipher  main.py 
```

The `cipher.exe` file can be found in `./dist`

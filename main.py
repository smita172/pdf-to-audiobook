import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename
from tkinter import Tk

# Hide the root Tkinter window
root = Tk()
root.withdraw()

# Open file dialog
book = askopenfilename()

# Use PdfReader (new syntax)
pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

# Initialize TTS engine
player = pyttsx3.init()

# Loop through PDF pages and read them aloud
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text:
        player.say(text)

player.runAndWait()

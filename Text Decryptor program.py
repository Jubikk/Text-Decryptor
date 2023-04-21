#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.2|

import time
import tkinter as tkinter
from PIL import Image, ImageTk
import requests
from io import BytesIO

def decrypt_text():
    encrypted_text = entry.get()
    plain_text = ""

    for char in encrypted_text:
        if char == '*':
            plain_text += 'a'
        elif char == '&':
            plain_text += 'e'
        elif char == '#':
            plain_text += 'i'
        elif char == '+':
            plain_text += 'o'
        elif char == '!':
            plain_text += 'u'
        else:
            plain_text += char

    #font format
    root.after(500, lambda:output_label.config(text="The decrypted text is: " + plain_text, font=('Times New Roman', 25, 'bold')))
    
    # load and display the GIF url
    response = requests.get("https://media.makeameme.org/created/well-done-you-50d10ff28b.jpg")
    img = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(img)
    root.after(1000, lambda:output_label.config(img_label.config(image=photo)))
    img_label.image = photo



import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('QR Code')
root.geometry("230x265")
my_label = Label(root)

# String which represents the QR code
e = Entry(root, width=50)
e.pack()


def qrCode():
    # Generate QR code
    www = e.get()
    url = pyqrcode.create(www)
    # Create and save the svg file naming "myqr.svg"
    url.svg(www+".svg", scale=8)
    # Create and save the png file naming "myqr.png"
    url.png(www+'.png', scale=6)
    create_image(www)

def create_image(www):
    clear_text()
    qrImg = www + ".png"
    my_img = ImageTk.PhotoImage(Image.open(qrImg))
    my_label.config(image=my_img)
    my_label.image = my_img
    my_label.pack()

    
def clear_text():
    e.delete(0, END)





myButton = Button(root, text="Enter your website", command=qrCode)
myButton.pack()
root.mainloop()
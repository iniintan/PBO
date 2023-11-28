import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from fungsi import hitung_luas, hitung_volume

def hitung():
    hasil_luas = hitung_luas(txtpanjang.get(),txtlebar.get(),txttinggi.get())
    hasil_volume = hitung_volume(txtpanjang.get(),txtlebar.get(),txttinggi.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtVolume.delete(0,END)
    txtVolume.insert(END,hasil_volume)

app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Balok")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="Intan Sulastri_220511166")
nama.grid(row=0, column=1, sticky=W, padx=5, pady=5)

panjang = Label(frame, text="panjang:")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

lebar = Label(frame, text="lebar:")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtlebar = Entry(frame)
txtlebar.grid(row=2, column=1)

tinggi = Label(frame, text="tinggi:")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txttinggi = Entry(frame)
txttinggi.grid(row=3, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
import tkinter as tk

pencere = tk.Tk()

selam = tk.Label(text="Merhaba Dünya!", fg="red",bg="yellow")
selam.pack()

butonOrnegi = tk.Button(text="Bana tıkla!",width=50,height=30)
butonOrnegi.pack()

pencere.mainloop()
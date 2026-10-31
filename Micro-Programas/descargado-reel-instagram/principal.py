from tkinter import *
from tkinter import messagebox #para mensajes emerjentes
from tkinter import filedialog
import yt_dlp

class Principal():
    def __init__(self):
        self.ven = Tk()

        ancho_ventana = 420 
        alto_ventana = 220

        ancho_pantalla = self.ven.winfo_screenwidth()  # 🖥️ Ancho total de pantalla / Total screen width
        alto_pantalla = self.ven.winfo_screenheight()  # 🖥️ Alto total de pantalla / Total screen height  

        x = (ancho_pantalla // 2) - (ancho_ventana // 2)  # 📐 Posición horizontal centrada / Horizontal centered position
        y = (alto_pantalla // 2) - (alto_ventana // 2)  # 📐 Posición vertical centrada / Vertical centered position

        self.ven.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.ruta = ""; # inicalizamos la variable de ruta para evitar valores basura
        self.rutaTxt = StringVar(value="Sin direccion...")
        self.inicio() # mandamos a inicio

    def Descargar(self):
        url = self.dato.get().strip()
        print(url)
        if not url:
            messagebox.showerror("Error","No se a proporcionado la URL")
            return
        if not self.ruta:
            messagebox.showerror("Error","No se a proporcionado la \n Direccion para guardar archivo")
            return
    
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s', # nombre de nuestro archivo
            'paths': {'home': self.ruta}  # donde guardaremos el vi   
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                messagebox.showinfo("Listo","Video Descargado")
                self.dato.delete(0,END)
                return
        except Exception as e:
            messagebox.showerror("Error","No se ha descargado el video")

        

    def Examinar(self):
        self.ruta = filedialog.askdirectory(title="Selecciona dónde guardar el video")
        # self.rutaTxt = self.ruta
        self.rutaTxt.set(self.ruta) # actualziamos el label


    def inicio(self):
        self.label = Label(text="Escribe la URL del Reel:")  # 🏷️ Etiqueta de estado / Status label
        self.label.place(x=5,y=70)
        # self.placeholder = 'Escribe El url'
        self.dato = Entry(self.ven, fg = 'gray') #color de la caja de texto
        self.dato.place(x=130, y=70)

        self.labelRuta = Label(text="Escribe la ruta donde desea guardar:")  # 🏷️ Etiqueta de estado / Status label
        self.labelRuta.place(x=5,y=100)

        Button(self.ven, text = 'Examinar', command = self.Examinar).place(x=200, y=100)
        self.labelRuta = Label(textvariable=self.rutaTxt, wraplength=100,)
        self.labelRuta.place(x=280, y=100)


        Button(self.ven, text = 'Descargar', command = self.Descargar).place(x=180, y=150)
        
        # self.ven.
        self.ven.mainloop()

        





if __name__ == '__main__':
    app = Principal()
    # app.inicio()
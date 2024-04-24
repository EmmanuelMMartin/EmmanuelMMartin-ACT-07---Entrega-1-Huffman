import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class InterfazCompresorHuffman:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Huffman")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#EABAB0")

        self.etiqueta = tk.Label(ventana, text="SELECCIONA UN ARCHIVO", font=("Verdana", 18, "bold"), bg="#EABAB0")  
        self.etiqueta.pack(pady=10)

        self.btn_salir = tk.Button(ventana, text="Salir", font=("Verdana", 12), command=self.salir)
        self.btn_salir.pack(pady=5, side="bottom", padx=5)

        self.btn_descomprimir = tk.Button(ventana, text="Descomprimir Archivo", font=("Verdana", 12))
        self.btn_descomprimir.pack(pady=5, side="bottom", padx=5)

        self.btn_comprimir = tk.Button(ventana, text="Comprimir Archivo", font=("Verdana", 12))
        self.btn_comprimir.pack(pady=5, side="bottom", padx=5)
        
        self.btn_mostrar_frecuencias = tk.Button(ventana, text="Mostrar Frecuencias", font=("Verdana", 12))
        self.btn_mostrar_frecuencias.pack(pady=5, side="bottom", padx=5)
        
        self.btn_mostrar_contenido = tk.Button(ventana, text="Mostrar Contenido", font=("Verdana", 12))
        self.btn_mostrar_contenido.pack(pady=5, side="bottom", padx=5)
        
        self.btn_examinar = tk.Button(ventana, text="Examinar Archivo", font=("Verdana", 12), command=self.examinar_archivo)
        self.btn_examinar.pack(pady=5, side="bottom", padx=5)

    def examinar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            messagebox.showinfo("Información", f"Archivo seleccionado: {archivo}")

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazCompresorHuffman(ventana)
    ventana.mainloop()

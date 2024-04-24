# Importamos las librerías necesarias
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import heapq

# Definimos la clase para representar un nodo en el árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, other):
        return self.frecuencia < other.frecuencia

# Definimos la clase para el compresor Huffman
class CompresorHuffman:
    def __init__(self, archivo):
        self.archivo = archivo
        self.frecuencias = {}  # Diccionario para almacenar las frecuencias de los caracteres
        self.codigos = {}  # Diccionario para almacenar los códigos Huffman de los caracteres
        self.arbol_huffman = None  # Representa el árbol de Huffman

    def calcular_frecuencias(self):
        # Método para calcular las frecuencias de los caracteres en el archivo
        with open(self.archivo, 'r') as archivo:
            for linea in archivo:
                for caracter in linea:
                    if caracter in self.frecuencias:
                        self.frecuencias[caracter] += 1
                    else:
                        self.frecuencias[caracter] = 1
        return self.frecuencias

    def construir_arbol_huffman(self):
        # Método para construir el árbol de Huffman a partir de las frecuencias
        lista_nodos = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in self.frecuencias.items()]
        heapq.heapify(lista_nodos)
        while len(lista_nodos) > 1:
            nodo_izquierdo = heapq.heappop(lista_nodos)
            nodo_derecho = heapq.heappop(lista_nodos)
            nuevo_nodo = NodoHuffman(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
            nuevo_nodo.izquierda = nodo_izquierdo
            nuevo_nodo.derecha = nodo_derecho
            heapq.heappush(lista_nodos, nuevo_nodo)
        self.arbol_huffman = lista_nodos[0]

    def generar_codigos_huffman_recursivo(self, nodo_actual, codigo_actual):
        # Método recursivo para generar los códigos Huffman de los caracteres
        if nodo_actual.caracter is not None:
            self.codigos[nodo_actual.caracter] = codigo_actual
        else:
            self.generar_codigos_huffman_recursivo(nodo_actual.izquierda, codigo_actual + '0')
            self.generar_codigos_huffman_recursivo(nodo_actual.derecha, codigo_actual + '1')

    def generar_codigos_huffman(self):
        # Método para generar los códigos Huffman de los caracteres
        self.generar_codigos_huffman_recursivo(self.arbol_huffman, '')

    def comprimir_archivo(self, archivo_comprimido):
        # Método para comprimir el archivo utilizando los códigos Huffman
        with open(self.archivo, 'r') as entrada, open(archivo_comprimido, 'wb') as salida:
            bits = ""
            for linea in entrada:
                for caracter in linea:
                    bits += self.codigos[caracter]
                    while len(bits) >= 8:
                        byte = int(bits[:8], 2)
                        salida.write(bytes([byte]))
                        bits = bits[8:]
            if bits:
                padding = 8 - len(bits)
                bits += '0' * padding
                byte = int(bits, 2)
                salida.write(bytes([byte]))
                salida.write(bytes([padding]))

    def descomprimir_archivo(self, archivo_comprimido, archivo_descomprimido):
        # Método para descomprimir el archivo comprimido
        with open(archivo_comprimido, 'rb') as entrada, open(archivo_descomprimido, 'w') as salida:
            bit_string = ""
            byte = entrada.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = entrada.read(1)
            padding = int(bit_string[-8:], 2)
            bit_string = bit_string[:-8-padding]
            nodo_actual = self.arbol_huffman
            for bit in bit_string:
                if bit == '0':
                    nodo_actual = nodo_actual.izquierda
                else:
                    nodo_actual = nodo_actual.derecha
                if nodo_actual.caracter is not None:
                    salida.write(nodo_actual.caracter)
                    nodo_actual = self.arbol_huffman

# Definimos la clase para la interfaz del compresor Huffman
class InterfazCompresorHuffman:
    def __init__(self, ventana):
        # Método para inicializar la interfaz
        self.ventana = ventana
        self.ventana.title("Compresor Huffman")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#EABAB0")  # Color de fondo

        # Etiqueta de título
        self.etiqueta = tk.Label(ventana, text="SELECCIONA UN ARCHIVO", font=("Verdana", 18, "bold"), bg="#EABAB0")  
        self.etiqueta.pack(pady=10)

        # Botón para salir
        self.btn_salir = tk.Button(ventana, text="Salir", font=("Verdana", 12), command=self.salir)
        self.btn_salir.pack(pady=5, side="bottom", padx=5)

        # Botón para descomprimir archivo
        self.btn_descomprimir = tk.Button(ventana, text="Descomprimir Archivo", font=("Verdana", 12), command=self.descomprimir_archivo)
        self.btn_descomprimir.pack(pady=5, side="bottom", padx=5)

        # Botón para comprimir archivo
        self.btn_comprimir = tk.Button(ventana, text="Comprimir Archivo", font=("Verdana", 12), command=self.comprimir_archivo)
        self.btn_comprimir.pack(pady=5, side="bottom", padx=5)
        
        # Botón para mostrar frecuencias de caracteres
        self.btn_mostrar_frecuencias = tk.Button(ventana, text="Mostrar Frecuencias", font=("Verdana", 12), command=self.mostrar_frecuencias)
        self.btn_mostrar_frecuencias.pack(pady=5, side="bottom", padx=5)
        
        # Botón para mostrar contenido del archivo
        self.btn_mostrar_contenido = tk.Button(ventana, text="Mostrar Contenido", font=("Verdana", 12), command=self.mostrar_contenido)
        self.btn_mostrar_contenido.pack(pady=5, side="bottom", padx=5)
        
        # Botón para examinar archivo
        self.btn_examinar = tk.Button(ventana, text="Examinar Archivo", font=("Verdana", 12), command=self.examinar_archivo)
        self.btn_examinar.pack(pady=5, side="bottom", padx=5)


        # Creamos una instancia del compresor Huffman
        self.compresor = CompresorHuffman(None)

    def examinar_archivo(self):
        # Método para seleccionar un archivo
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.compresor.archivo = archivo
            messagebox.showinfo("Información", f"Archivo seleccionado: {archivo}")

    def mostrar_frecuencias(self):
        # Método para mostrar las frecuencias de caracteres del archivo
        if self.compresor.archivo:
            frecuencias = self.compresor.calcular_frecuencias()
            mensaje = "Frecuencias de caracteres:\n"
            for caracter, frecuencia in frecuencias.items():
                mensaje += f"{caracter}: {frecuencia}\n"
            messagebox.showinfo("Frecuencias de Caracteres", mensaje)
        else:
            messagebox.showerror("Error", "Por favor, seleccione un archivo primero.")

    def mostrar_contenido(self):
        # Método para mostrar el contenido del archivo
        if self.compresor.archivo:
            with open(self.compresor.archivo, 'r') as archivo:
                contenido = archivo.read()
                messagebox.showinfo("Contenido del Archivo", contenido)
        else:
            messagebox.showerror("Error", "Por favor, seleccione un archivo primero.")

    def comprimir_archivo(self):
        # Método para comprimir el archivo
        if self.compresor.archivo:
            self.compresor.calcular_frecuencias()
            self.compresor.construir_arbol_huffman()
            self.compresor.generar_codigos_huffman()
            archivo_comprimido = self.compresor.archivo + ".huf"
            self.compresor.comprimir_archivo(archivo_comprimido)
            messagebox.showinfo("Compresión Completada", f"Archivo comprimido guardado como {archivo_comprimido}")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un archivo primero.")

    def descomprimir_archivo(self):
        # Método para descomprimir el archivo comprimido
        archivo_comprimido = filedialog.askopenfilename(filetypes=[("Archivos comprimidos", "*.huf")])
        if archivo_comprimido:
            archivo_descomprimido = archivo_comprimido[:-4] + "_descomprimido.txt"
            self.compresor.descomprimir_archivo(archivo_comprimido, archivo_descomprimido)
            messagebox.showinfo("Descompresión Completada", f"Archivo descomprimido guardado como {archivo_descomprimido}")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un archivo comprimido primero.")

    def salir(self):
        # Método para cerrar la ventana
        self.ventana.destroy()

# Crear la ventana principal y la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazCompresorHuffman(ventana)
    ventana.mainloop()

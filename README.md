# EmmanuelMMartin-ACT-07---Entrega-1-Huffman
Crear un programa en  Python que comprima un archivo de texto utilizando el algoritmo de compresión de Huffman.

REPORTE
Introducción
El método de Huffman, desarrollado por David A. Huffman en 1952, es un algoritmo de compresión sin pérdida utilizado para reducir el tamaño de los archivos al asignar códigos binarios más cortos a los caracteres más frecuentes y códigos más largos a los caracteres menos frecuentes. Esto se logra construyendo un árbol de Huffman, donde cada hoja del árbol representa un carácter del archivo y la ruta desde la raíz hasta la hoja determina el código binario asignado a ese carácter.
El objetivo de este informe es proporcionar una visión general del método de Huffman y explicar cómo se implementa este algoritmo en el código de Python proporcionado.

Objetivos
•	Aprender la Implementación del Método de Huffman.
•	Comprender los fundamentos teóricos del algoritmo de compresión de Huffman y su aplicación en la compresión de archivos.
•	Estudiar la estructura del árbol de Huffman y cómo se utiliza para asignar códigos de longitud variable a los caracteres del archivo.
•	Explorar el código proporcionado y comprender cómo se traducen los conceptos del algoritmo de Huffman en Python.
•	Identificar y explicar las diferentes partes del código, incluyendo las clases, métodos y estructuras de datos utilizadas.
•	Aplicar los Conceptos en un Proyecto Práctico.
•	Utilizar el conocimiento adquirido para desarrollar un compresor y descompresor de archivos funcionales en Python.
•	Implementar una interfaz gráfica de usuario para hacer que el programa sea más accesible y fácil de usar para los usuarios finales.
•	Experimentar con la Compresión y Descompresión de Archivos.
•	Realizar pruebas utilizando diferentes archivos de texto para comprender el rendimiento del compresor de Huffman en una variedad de escenarios.
•	Observar cómo cambia el tamaño del archivo comprimido en función de la frecuencia de los caracteres y la estructura del texto.

Explicación del código 
Backend (Compresor Huffman):
Clase NodoHuffman:
•	Esta clase define la estructura de un nodo en el árbol de Huffman. Cada nodo tiene los siguientes atributos:
•	caracter: El carácter representado por el nodo.
•	frecuencia: La frecuencia del carácter en el archivo.
•	izquierda y derecha: Referencias a los nodos hijos izquierdo y derecho, respectivamente.
•	Además, la clase sobrecarga el operador de comparación < para permitir la comparación de nodos basada en sus frecuencias.
Clase CompresorHuffman:
Esta clase contiene los métodos necesarios para comprimir y descomprimir archivos utilizando el algoritmo de Huffman.
•	__init__(): El método de inicialización recibe la ruta del archivo a ser comprimido o descomprimido.
•	calcular_frecuencias(): Este método calcula las frecuencias de los caracteres en el archivo y devuelve un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
•	construir_arbol_huffman(): Construye el árbol de Huffman utilizando una cola de prioridad (heap).
•	generar_codigos_huffman(): Genera los códigos Huffman asignados a cada carácter del archivo.
•	comprimir_archivo(): Comprime el archivo utilizando los códigos Huffman generados.
•	descomprimir_archivo(): Descomprime el archivo comprimido utilizando el árbol de Huffman construido previamente.
Frontend (Interfaz Gráfica):
Clase InterfazCompresorHuffman:
•	Esta clase define la interfaz gráfica del programa utilizando la biblioteca Tkinter.
•	Inicializa una ventana con botones para seleccionar un archivo, mostrar frecuencias de caracteres, mostrar contenido del archivo, comprimir y descomprimir archivos.
•	Cada botón está vinculado a un método que ejecuta la funcionalidad correspondiente.
•	Se utilizan cuadros de mensaje emergente para proporcionar información y alertas al usuario.
Funcionamiento General:
•	El usuario selecciona un archivo de texto utilizando el botón "Examinar Archivo".
•	Se pueden mostrar las frecuencias de los caracteres del archivo seleccionado haciendo clic en el botón "Mostrar Frecuencias".
•	El contenido completo del archivo puede mostrarse haciendo clic en el botón "Mostrar Contenido".
•	Al hacer clic en el botón "Comprimir Archivo", el archivo seleccionado se comprime utilizando el algoritmo de Huffman.
•	Para descomprimir un archivo comprimido, el usuario selecciona el archivo utilizando el botón "Descomprimir Archivo".

Conclusión Personal
La práctica de implementar el algoritmo de Huffman en Python ha sido una experiencia enriquecedora. A través de este proyecto, he comprendido mejor cómo funciona la compresión de archivos y cómo se pueden aplicar conceptos algorítmicos para lograr una reducción efectiva del tamaño de los archivos sin pérdida de datos.
Además, el desarrollo de la interfaz gráfica ha añadido un componente interactivo al proyecto, lo que lo hace más accesible y fácil de usar para los usuarios finales.
En resumen, esta práctica ha sido una oportunidad invaluable para fortalecer mis habilidades en programación y comprensión de algoritmos, y estoy ansioso por explorar más aplicaciones y mejoras en el futuro.


Bibliografía 
•	https://persoal.citius.usc.es/eva.cernadas/informaticaparacientificos/material/libros/Python%20 para%20todos.pdf 
 
 

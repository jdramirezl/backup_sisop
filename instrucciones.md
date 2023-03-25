## Práctica: Crear un programa de copia de seguridad de archivos y restauración del archivo backup

### Objetivo

El objetivo de esta práctica evaluable es crear un programa que permita realizar una copia de seguridad de una carpeta en fragmentos de 512 MB, y otro programa que permita restaurar la copia de seguridad a su estado original. El programa debe ser capaz de trabajar con archivos de cualquier tamaño.

### Parte 1: Crear el programa de copia de seguridad

El programa de copia de seguridad debe cumplir los siguientes requisitos:

* Recibir como entrada la ruta de la carpeta que se desea copiar y la ruta de la carpeta donde se guardarán los fragmentos de la copia de seguridad.
* Dividir los archivos de la carpeta original en varios fragmentos de tamaño máximo de 512 MB, y guardarlos en la carpeta de la copia de seguridad.
* Nombrar los fragmentos de la copia de seguridad de forma que se pueda identificar fácilmente a qué carpeta pertenecen y en qué orden deben ser restaurados.
* Imprimir un mensaje indicando que la copia de seguridad se ha completado con éxito.
* Crear un archivo en formato JSON con la composición del archivo backup, es decir, con los archivos respaldados, sus tamaño y cuantos archivos de 512 MB ser crearon.

### Parte 2: Crear el programa de restauración

El programa de restauración debe cumplir los siguientes requisitos:

* Recibir como entrada la ruta de la carpeta de la copia de seguridad y la ruta de la carpeta donde se restaurarán los archivos.
* Leer los fragmentos de la carpeta de la copia de seguridad en el orden adecuado y restaurarlos en la carpeta original.
* Imprimir un mensaje indicando que la restauración se ha completado con éxito.

### Entrega

Una vez completada la práctica, se debe entregar un archivo comprimido con los siguientes elementos:

* El código fuente de los programas de copia de seguridad y restauración.
* Un archivo README que explique cómo utilizar los programas y cualquier otra información relevante.

La entrega se completa con la sustentación.

### Preguntas adicionales

Si tienes alguna pregunta adicional sobre la práctica, no dudes en hacerla. Estoy aquí para ayudarte en lo que necesites.

**

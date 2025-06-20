# Algoritmo path

Se te proporciona una ruta absoluta de un sistema de archivos al
 estilo Unix, la cual siempre comienza con una barra diagonal '/'.
  Tu tarea es transformar esta ruta absoluta en su ruta canónica simplificada.

Las reglas de un sistema de archivos al estilo Unix son las siguientes:

- Un solo punto . representa el directorio actual.

- Dos puntos .. representan el directorio anterior o padre.

- Varias barras consecutivas como // o /// se tratan como una sola barra /.

Cualquier secuencia de puntos que no coincida con las reglas anteriores debe 
tratarse como un nombre válido de archivo o directorio.
 Por ejemplo, '...' y '....' son nombres válidos.

La ruta canónica simplificada debe cumplir estas reglas:

La ruta debe comenzar con una única barra diagonal /.

Los directorios dentro de la ruta deben estar separados por exactamente una barra /.

La ruta no debe terminar con una barra /, a menos que sea el directorio raíz.

La ruta no debe contener puntos . ni dobles puntos .. que indiquen directorios actuales o padres.

Devuelve la ruta canónica simplificada.

Ejemplos:
Ejemplo 1:
Entrada: path = "/home/"
Salida: "/home"
Explicación:
La barra al final debe ser eliminada.

Ejemplo 2:
Entrada: path = "/home//foo/"
Salida: "/home/foo"
Explicación:
Múltiples barras consecutivas se reemplazan por una sola.

Ejemplo 3:
Entrada: path = "/home/user/Documents/../Pictures"
Salida: "/home/user/Pictures"
Explicación:
.. indica subir un nivel (al directorio padre).

Ejemplo 4:
Entrada: path = "/../"
Salida: "/"
Explicación:
No se puede subir un nivel desde el directorio raíz.

Ejemplo 5:
Entrada: path = "/.../a/../b/c/../d/./"
Salida: "/.../b/d"
Explicación:
"..." se trata como un nombre de directorio válido.

Restricciones:
1 <= path.length <= 3000

El path consiste en letras en inglés, dígitos, punto '.', barra '/' o guion bajo '_'.

El path es una ruta absoluta válida del estilo Unix.
# Respuestas de analisis - Taller Semana 8

Responde con tus propias palabras despues de ejecutar y verificar el programa.

## 1. Que problema resuelve el programa?

Respuesta:
El programa ayuda a digitalizar y automatizar el control de producción en una finca. Resuelve el problema de tener que hacer cálculos manuales de totales y promedios, permitiendo saber rápidamente si la producción de leche y maíz está dentro de los niveles normales.

## 2. Que datos de entrada solicita?

Respuesta:
Primero solicita el número de días que se van a registrar. Luego, para cada uno de esos días, pide ingresar los litros de leche producidos y los kilos de maíz cosechados.


## 3. Que resultados muestra?

Respuesta:
Al finalizar, muestra un resumen con:

El total de días registrados.

El total y promedio diario de litros de leche.

El total y promedio diario de kilos de maíz.

Mensajes de alerta (OK) indicando si los promedios son estables según los límites del sistema.


## 4. Que estructura repetitiva usa el programa?

Respuesta:
Usa un ciclo "for" (o para). Esto se nota porque el programa repite las mismas preguntas ("Ingrese litros...") exactamente la cantidad de veces que indicamos al principio (en este caso, 5 días).


## 5. Que condicionales usa para generar alertas?

Respuesta:
Usa la estructura "if" (si). El programa evalúa si el promedio calculado es mayor o igual a un límite definido; si se cumple, muestra el mensaje "OK" indicando que la producción es estable.


## 6. Que error puede aparecer si ejecutas mal el archivo?

Respuesta:
El error más común es el FileNotFoundError si intentas ejecutar el comando sin estar en la carpeta correcta, o un error de sintaxis si escribes mal python o la ruta del archivo src/produccion_finca.py.


## 7. Como verificaste que los resultados eran correctos?

Respuesta:
Lo verifiqué haciendo un cálculo manual: sumé todos los valores de leche (que dieron 50) y maíz (que dieron 120) y dividí por los 5 días registrados. Al ver que los resultados coincidían con la terminal, confirmé que el programa funciona bien.


## 8. Que ajuste harias para adaptar el programa a otro producto rural?

Respuesta:
Cambiaría los nombres de las variables y los textos de entrada. Por ejemplo, en lugar de "litros de leche", podría pedir "kilos de café" o "cantidad de huevos", y ajustaría los límites de las alertas según lo que se considere una producción estable para esos productos.


## 9. Que evidencia demuestra que ejecutaste correctamente el programa?

Respuesta:
La captura de pantalla llamada `captura_04_programa_ejecutado.png` , donde se ve la terminal de VS Code con todos los datos ingresados, los cálculos finales realizados por el script y el mensaje de proceso finalizado.


## 10. Que aprendiste sobre el uso de VS Code?

Respuesta:
Aprendí que es una herramienta muy completa que permite escribir el código y probarlo ahí mismo usando la terminal integrada, y que mantener los archivos organizados en carpetas como src facilita mucho el trabajo en equipo.


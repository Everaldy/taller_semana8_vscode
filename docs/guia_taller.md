# Guia del taller - Semana 8

## Nombre de la actividad
Practica guiada en el entorno: logica, resolucion de problemas y ejecucion de programas.

## Tema
Ejercicios practicos de logica y resolucion de problemas; ejecucion de programas.

## Modalidad
Individual o en parejas.

## Medio de entrega
Moodle.

## Evidencias solicitadas
- Capturas o registro de acciones.
- Bitacora con pasos y resultados.
- Programa ejecutado.
- Verificacion de resultados.
- Ajustes realizados si aparecen errores.

---

# 1. Situacion problema

En una finca rural se necesita registrar la produccion durante varios dias. Cada dia se anotan dos datos:

1. Litros de leche producidos.
2. Kilos de maiz cosechados.

El dueno de la finca necesita conocer:

- Total de leche producida.
- Promedio diario de leche.
- Total de maiz cosechado.
- Promedio diario de maiz.
- Alertas si la produccion promedio esta por debajo de un limite esperado.

---

# 2. Objetivo del taller

Usar Visual Studio Code para abrir un proyecto, navegar por sus carpetas, ejecutar un programa en Python, analizar resultados, corregir posibles errores y documentar el proceso mediante capturas y bitacora.

---

# 3. Conceptos que se aplican

| Concepto | Aplicacion en el taller |
|---|---|
| Logica de programacion | Comprender el problema y organizar pasos para resolverlo. |
| Algoritmo | Definir la secuencia: pedir datos, sumar, promediar y mostrar resultados. |
| Variable | Guardar datos como litros de leche, kilos de maiz y totales. |
| Ciclo | Repetir el registro por cada dia. |
| Condicional | Mostrar alertas si el promedio es bajo. |
| Ejecucion | Correr el programa en la terminal de VS Code. |
| Verificacion | Comparar el resultado del programa con calculos manuales. |
| Ajuste | Corregir errores de datos, comandos o codigo si aparecen. |

---

# 4. Paso a paso en Visual Studio Code

## Paso 1: Abrir la carpeta del proyecto

1. Abre Visual Studio Code.
2. Ve al menu `File > Open Folder` o `Archivo > Abrir carpeta`.
3. Selecciona la carpeta del taller.
4. Verifica que se vean las carpetas `src`, `docs` y `evidencias`.

**Evidencia:** toma una captura del explorador de archivos de VS Code.

---

## Paso 2: Identificar paneles y menus

Ubica los siguientes elementos:

- Panel del explorador.
- Archivo `src/produccion_finca.py`.
- Menu `Terminal`.
- Terminal integrada.
- Area del editor de codigo.

**Evidencia:** en la bitacora escribe que paneles y menus encontraste.

---

## Paso 3: Abrir el programa

1. En el panel izquierdo, abre la carpeta `src`.
2. Haz clic en `produccion_finca.py`.
3. Lee los comentarios iniciales del programa.

**Evidencia:** toma una captura del codigo abierto en VS Code.

---

## Paso 4: Guardar el archivo

Usa el atajo:

```text
Ctrl + S
```

Esto asegura que cualquier cambio quede guardado antes de ejecutar.

---

## Paso 5: Abrir la terminal integrada

Puedes hacerlo de dos maneras:

- Menu: `Terminal > New Terminal`.
- Atajo: `Ctrl + ``.

**Evidencia:** toma una captura de la terminal abierta.

---

## Paso 6: Ejecutar el programa

Escribe en la terminal:

```bash
python src/produccion_finca.py
```

Si no funciona, intenta:

```bash
python3 src/produccion_finca.py
```

---

## Paso 7: Ingresar datos de prueba

Usa estos datos para la primera prueba:

| Dia | Leche | Maiz |
|---|---:|---:|
| 1 | 10 | 25 |
| 2 | 12 | 30 |
| 3 | 8 | 20 |
| 4 | 15 | 35 |
| 5 | 5 | 10 |

Resultados esperados:

- Total de leche: 50 litros.
- Promedio de leche: 10 litros.
- Total de maiz: 120 kilos.
- Promedio de maiz: 24 kilos.

**Evidencia:** toma una captura del resultado en la terminal.

---

## Paso 8: Verificar resultados

Compara el resultado del programa con los calculos manuales.

Formula usada:

```text
promedio = total / numero de dias
```

Si el resultado no coincide, revisa:

1. Si digitaste bien los datos.
2. Si ejecutaste el archivo correcto.
3. Si guardaste el archivo antes de ejecutar.
4. Si estas ubicado en la carpeta correcta.

---

## Paso 9: Probar un caso con alerta

Ejecuta nuevamente el programa y usa datos bajos para leche o maiz.

Ejemplo:

| Dia | Leche | Maiz |
|---|---:|---:|
| 1 | 4 | 10 |
| 2 | 5 | 12 |
| 3 | 6 | 9 |

Observa si el programa muestra alerta.

---

## Paso 10: Registrar la bitacora

Abre el archivo:

```text
docs/bitacora_estudiante.md
```

Completa:

- Fecha.
- Integrantes.
- Pasos realizados.
- Comandos usados.
- Resultados obtenidos.
- Errores encontrados.
- Ajustes realizados.
- Reflexion final.

---

# 5. Preguntas de analisis

Responde en `docs/respuestas_analisis.md`:

1. Que problema resuelve el programa?
2. Que datos de entrada solicita?
3. Que resultados muestra?
4. Que estructura repetitiva usa el programa?
5. Que condicionales usa para generar alertas?
6. Que error puede aparecer si ejecutas mal el archivo?
7. Como verificaste que los resultados eran correctos?
8. Que ajuste harias para adaptar el programa a otro producto rural?

---

# 6. Cierre de la actividad

Al finalizar, comprime la carpeta del proyecto y subela a Moodle junto con las capturas y la bitacora diligenciada.

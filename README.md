# Taller Semana 8 - Logica, resolucion de problemas y ejecucion de programas

## Tema
Ejercicios practicos de logica y resolucion de problemas; ejecucion de programas.

## Proposito del taller
Este proyecto esta disenado para abrirse en Visual Studio Code y desarrollar una practica guiada paso a paso. El estudiante debera navegar por paneles y menus del IDE, usar comandos y atajos, ejecutar un programa, verificar resultados, ajustar procedimientos y registrar evidencias mediante capturas y bitacora.

## Producto a entregar
Al finalizar, el estudiante debe entregar en Moodle:

1. Carpeta comprimida del proyecto o archivo de respuesta indicado por el docente.
2. Capturas del proceso en la carpeta `evidencias/capturas`.
3. Bitacora diligenciada en `docs/bitacora_estudiante.md`.
4. Codigo ejecutado correctamente en `src/produccion_finca.py`.
5. Respuestas de analisis en `docs/respuestas_analisis.md`.

## Estructura del proyecto

```text
semana8-taller-vscode/
├── README.md
├── src/
│   └── produccion_finca.py
├── docs/
│   ├── guia_taller.md
│   ├── bitacora_estudiante.md
│   ├── respuestas_analisis.md
│   ├── glosario_comandos_menus.md
│   └── criterios_evaluacion.md
├── evidencias/
│   ├── capturas/
│   │   └── instrucciones_capturas.md
│   └── registro_acciones.md
└── .vscode/
    ├── settings.json
    └── tasks.json
```

## Como ejecutar el programa

### Opcion 1: desde la terminal de VS Code

1. Abre esta carpeta en Visual Studio Code.
2. Abre la terminal integrada con el menu `Terminal > New Terminal`.
3. Ejecuta:

```bash
python src/produccion_finca.py
```

En algunos equipos puede ser necesario usar:

```bash
python3 src/produccion_finca.py
```

### Opcion 2: usando la tarea de VS Code

1. Abre el menu `Terminal > Run Task...`.
2. Selecciona `Ejecutar taller Semana 8`.
3. Observa los resultados en la terminal.

## Atajos sugeridos

| Accion | Atajo |
|---|---|
| Guardar archivo | Ctrl + S |
| Buscar texto | Ctrl + F |
| Abrir terminal | Ctrl + ` |
| Copiar | Ctrl + C |
| Pegar | Ctrl + V |
| Deshacer | Ctrl + Z |

## Recomendacion
Antes de ejecutar el programa, lee completamente `docs/guia_taller.md`.

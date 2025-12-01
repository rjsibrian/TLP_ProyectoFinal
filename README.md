# Proyecto final – Mini parser de inglés + demo NLP con spaCy

Este repositorio contiene dos componentes:

1. **mini_parser_en**: un analizador sintáctico recursivo para oraciones simples en inglés, con verificación de concordancia (sujeto–verbo, determinante–sustantivo) y manejo básico de errores.
2. **nlp_implementation**: una demostración de procesamiento de lenguaje natural usando **spaCy**, aplicada a un archivo de frases de ejemplo.

---

## 1. Estructura del repositorio

```text
TLP_ProyectoFinal/
├── mini_parser_en/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── en_lexicon.py    # Léxico reducido y tokenización
│   │   ├── en_parser.py     # Parser descendente recursivo
│   │   └── run_en.py        # Punto de entrada por consola
│   └── test/
│       ├── valid.txt        # Oraciones válidas
│       └── invalid.txt      # Oraciones inválidas
├── nlp_implementation/
│   ├── demo_spacy.py        # Script de análisis con spaCy
│   └── frases_input.txt     # Frases de entrada para spaCy
├── Informe Fase 2.pdf
└── README.md
```

---

## 2. Requisitos

### Generales

- Python 3.8 o superior  
- `pip` instalado y funcionando

### Para el mini parser (`mini_parser_en`)

- **No requiere librerías externas**: solo módulos estándar de Python.

### Para la demo de NLP (`nlp_implementation`)

- Librería **spaCy**
- Modelo de inglés `en_core_web_sm`

Las instrucciones para instalarlo están en la sección 4.

---

## 3. Uso del mini parser (mini_parser_en)

> Todas las instrucciones estan en la carpeta raíz del proyecto  
> `TLP_ProyectoFinal/Informe Fase 2`.

### 3.1. Analizar una sola oración

```bash
cd mini_parser_en
python -m src.run_en "the boys eat"
```

Salida esperada (oración válida):

```text
✔ Parsing successful.
```

Ejemplo de oración inválida:

```bash
python -m src.run_en "book eats"
```

Salida típica:

```text
✘ Errors found:
  1. Grammar Error: Countable singular noun 'book' cannot appear without a determiner.
```

### 3.2. Analizar un archivo de oraciones

`test/valid.txt` y `test/invalid.txt` contienen ejemplos de prueba, una oración por línea.

```bash
cd mini_parser_en
python -m src.run_en -f test/valid.txt
python -m src.run_en -f test/invalid.txt
```

Salida típica:

```text
[OK] the boy eats
[OK] the boys eat
[ERROR] book eats
   -> Grammar Error: ...
[ERROR] the boys eats
   -> Subject–Verb Agreement Error: ...
```

### 3.3. Resumen rápido de funcionamiento interno

- `en_lexicon.py`:
  - Define la clase `Token` y un **léxico reducido** (determinantes, pronombres, sustantivos, verbos, adjetivos, preposiciones).
  - La función `tokenize_sentence(sentence)` convierte una cadena en una lista de tokens y lanza `LexicalError` si encuentra una palabra desconocida.
- `en_parser.py`:
  - Implementa un **parser descendente recursivo** para la gramática básica `S -> NP VP`.
  - Valida:
    - Concordancia **sujeto–verbo** (singular/plural).
    - Concordancia **determinante–sustantivo**.
    - Restricción de sustantivo contable singular sin determinante.
  - Permite analizar varias oraciones y acumular mensajes de error.

---

## 4. Uso de la demo NLP con spaCy

> Todas las instrucciones estan en la carpeta raíz del proyecto  
> `TLP_ProyectoFinal//Informe Fase 2`.

El script `demo_spacy.py` lee las frases de `frases_input.txt`, las procesa con spaCy y muestra por consola información lingüística (tokens, categorías, dependencias, etc.).  
Puedes editar `frases_input.txt` para probar tus propias oraciones.

### 4.1. Instalación en macOS

1. Instalar spaCy:

   ```bash
   pip install spacy
   ```

2. Descargar el modelo de inglés:

   ```bash
   python -m spacy download en_core_web_sm
   ```

3. Ejecutar el programa:

   ```bash
   cd nlp_implementation
   python3 demo_spacy.py
   ```

---

### 4.2. Instalación en Windows

1. Instalar spaCy (en PowerShell o CMD):

   ```bash
   pip install spacy
   ```

2. Descargar el modelo de inglés:

   ```bash
   python -m spacy download en_core_web_sm
   ```

3. Ejecutar el programa:

   ```bash
   cd nlp_implementation
   python demo_spacy.py
   ```

---

## 5. Ejemplo de ejecución (NLP)

Contenido de ejemplo en `frases_input.txt`:

```text
The boys eat apples.
The girl runs in the park.
Book eats.
```

Salida típica (resumen):

- Para cada frase, spaCy muestra:
  - tokens,
  - categoría gramatical (POS),
  - dependencias sintácticas,
  - otra información lingüística relevante.

---

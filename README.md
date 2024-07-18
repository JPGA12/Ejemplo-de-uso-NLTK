# Procesamiento de Lenguaje Natural con NLTK

Este código implementa un ejemplo básico de procesamiento de lenguaje natural (PLN) utilizando la biblioteca NLTK en Python. El código realiza las siguientes tareas:

- **Tokenización**: Divide el texto de entrada en palabras individuales (tokens).
- **Etiquetado de Partes del Discurso**: Asigna una etiqueta gramatical a cada palabra (sustantivo, verbo, adjetivo, etc.).
- **Análisis Sintáctico**: Utiliza una gramática formal para analizar la estructura sintáctica de la oración.
- **Análisis Semántico**: Asigna un significado básico a cada palabra.
- **Análisis de Discurso**: Identifica relaciones de discurso entre las palabras.

## Ejemplo de uso

1. Reemplace el texto de ejemplo "El procesamiento de lenguaje natural es fascinante." con el texto que desea analizar.
2. Ejecute el código en Python para obtener los resultados del procesamiento.

## Explicación detallada del código

### 1. Importación de bibliotecas

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import CFG
from nltk.parse import ChartParser
```
Se importan las bibliotecas necesarias de NLTK para realizar las tareas de PLN.

### 2. Descarga de recursos de NLTK
```python

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```
Se descargan los recursos necesarios de NLTK para la tokenización y el etiquetado de Partes del Discurso.

### 3. Definición del texto de ejemplo
``` python
text = "El procesamiento de lenguaje natural es fascinante."
```
Se define una variable text que contiene el texto de ejemplo a analizar.

### 4. Tokenización
```python
tokens = word_tokenize(text)
print("Tokens:", tokens)
```
La función word_tokenize divide el texto en palabras individuales y las almacena en una lista tokens.

### 5. Etiquetado de Partes del Discurso
```python
tags = pos_tag(tokens)
print("Tags:", tags)
```
La función pos_tag asigna una etiqueta gramatical a cada palabra en la lista tokens y las almacena en una lista tags.

### 6. Análisis Sintáctico
```python
grammar = CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP | V PP
  NP -> DT N | DT N PP | N
  PP -> P NP
  DT -> 'El' | 'la' | 'las' | 'una'
  N -> 'procesamiento' | 'lenguaje' | 'natural' | 'subdisciplina' | 'inteligencia' | 'artificial' | 'IA' | 'interacción' | 'computadoras' | 'lenguajes' | 'humanos' | 'objetivo' | 'aplicaciones' | 'sistemas' | 'traducción' | 'asistentes' | 'virtuales' | 'Siri' | 'Alexa' | 'análisis' | 'sentimientos' | 'redes' | 'sociales' | 'fases' | 'morfemas' | 'significado' | 'contextos' | 'gramaticales' | 'palabra' | 'niños' | 'raíz' | 'niño' | 'sufijo' | 'plural' | 'oración' | 'gato' | 'alfombra' | 'predicado' | 'sentido' | 'entidad' | 'financiera' | 'asiento' | 'párrafo' | 'documento' | 'María' | 'mercado' | 'ella' | 'frutas' | 'implicaturas' | 'actos' | 'habla' | 'solicitudes' | 'promesas' | 'órdenes' | 'herramientas' | 'librerías' | 'investigación' | 'desarrollo' | 'fascinante'
  V -> 'es' | 'ocup' | 'permit' | 'comprendan' | 'interpreten' | 'generen' | 'sean' | 'utilizan' | 'varían' | 'forman' | 'realizan' | 'identifican' | 'representan' | 'mencionan' | 'compró' | 'deben' | 'incluyen' | 'influye' | 'consideran' | 'proporcionan'
  P -> 'de' | 'en' | 'a' | 'entre' | 'como'
  PUNCT -> '.'
  S -> S PUNCT
""")
parser = ChartParser(grammar)
tree = list(parser.parse(tags))[0]
print("Parse Tree:")
tree.pretty_print()
```
Se define una gramática formal utilizando CFG.fromstring y se crea un ChartParser con esta gramática. Luego, se analiza la estructura sintáctica de las oraciones y se imprime el árbol de análisis.

# Conclusión
Este ejemplo básico de procesamiento de lenguaje natural demuestra cómo utilizar la biblioteca NLTK en Python para realizar tokenización, etiquetado de partes del discurso y análisis sintáctico. Puede expandir y modificar este ejemplo para adaptarse a necesidades más complejas de procesamiento de lenguaje natural.

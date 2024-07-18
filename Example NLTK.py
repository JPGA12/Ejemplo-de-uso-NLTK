import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import CFG
from nltk.parse import ChartParser

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Texto de ejemplo
text = "El procesamiento de lenguaje natural es fascinante."

# Tokenización: divide el texto en palabras o "tokens"
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Etiquetado de Partes del Discurso: asigna una etiqueta gramatical a cada token
tags = pos_tag(tokens)
print("Tags:", tags)

# Análisis Sintáctico: definición de la gramática
# CFG (Context-Free Grammar) define las reglas de formación de frases y oraciones en un lenguaje natural
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

# Realiza el análisis sintáctico usando la gramática definida y los tokens
for tree in parser.parse(tokens):
    print(tree)
    tree.draw()

# Análisis Semántico y de Discurso (simplificado para ilustración)
def analyze_semantics(tokens):
    # Diccionario simplificado de significados para un análisis semántico básico
    sem_dict = {
        'procesamiento': 'acción de procesar',
        'lenguaje': 'sistema de comunicación',
        'natural': 'relativo a la naturaleza',
        'fascinante': 'que fascina o cautiva'
    }
    # Asignar significado a cada token usando el diccionario
    semantics = {token: sem_dict.get(token, 'desconocido') for token in tokens}
    return semantics

semantics = analyze_semantics(tokens)
print("Análisis Semántico:", semantics)

def analyze_discourse(tokens):
    # Simulación de relaciones de discurso básicas
    discourse_relations = []
    # Relaciona cada determinante o preposición con la siguiente palabra
    for i, token in enumerate(tokens):
        if token.lower() in ['el', 'de', 'es']:
            discourse_relations.append((tokens[i], tokens[i+1]))
    return discourse_relations

discourse = analyze_discourse(tokens)
print("Análisis de Discurso:", discourse)

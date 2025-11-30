import spacy

# Cargar modelo de inglés
nlp = spacy.load("en_core_web_sm")

# Imprimir el árbol sintáctico completo de spaCy
def imprimir_arbol(token, nivel=0):
    indent = "  " * nivel
    print(f"{indent}- {token.text} ({token.dep_}, {token.pos_})")
    for child in token.children:
        imprimir_arbol(child, nivel + 1)

# Imprimir tokens, POS, dependencia, lema, rasgos
def imprimir_tokens(doc):
    print("\nTOKENS (POS, DEP, LEMMA, MORPH):")
    print("-" * 100)
    print(f"{'TOKEN':12} {'POS':10} {'DEP':12} {'LEMMA':12} {'MORPH'}")
    print("-" * 100)

    for tok in doc:
        print(f"{tok.text:12} {tok.pos_:10} {tok.dep_:12} {tok.lemma_:12} {tok.morph}")

# Imprimir subárboles (frases completas)
def imprimir_subarboles(doc):
    print("\nSUBÁRBOL{}\S (frases que cada token encabeza):")
    print("-" * 100)

    for tok in doc:
        frase = " ".join(t.text for t in tok.subtree)
        print(f"{tok.text:12} → {frase}")

def main():
    try:
        with open("frases_input.txt", "r", encoding="utf-8") as f:
            frases = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("No se encontró el archivo frases_input.txt")
        return

    for sentence in frases:
        print("\nORACIÓN:")
        print(sentence)
        print("=" * 100)

        doc = nlp(sentence)

        # 1. Tokens detallados
        imprimir_tokens(doc)

        # 2. Árbol sintáctico completo
        print("\nÁRBOL SINTÁCTICO (DEPENDENCY TREE):")
        print("-" * 100)
        root = [t for t in doc if t.dep_ == "ROOT"][0]
        imprimir_arbol(root)

        # 3. Subárboles
        imprimir_subarboles(doc)

if __name__ == "__main__":
    main()
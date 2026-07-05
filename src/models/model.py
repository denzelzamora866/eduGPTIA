class eduGPTIA:

    def __init__(self):
        self.name = "eduGPTIA"
        self.corpus = ""
        self.vocabulary = set()
        self.total_words = 0

    def show_information(self):
        print("=" * 45)
        print(f"{self.name} v0.0.1")
        print("=" * 45)
        print()

        print(f"Modelo: {self.name}")
        print("Estado: Activo")
        print(f"Corpus cargado: {self.total_words} palabras")
        print(f"Vocabulario: {len(self.vocabulary)} palabras")
        print()

        print("eduGPTIA:")
        print("Hola, todavía no sé nada.")
        print("Enséñame un libro.")
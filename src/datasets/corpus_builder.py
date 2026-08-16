from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]


class CorpusBuilder:

    def __init__(self):

        self.books_path = (
            BASE_DIR / "data" / "books"
        )

        self.processed_path = (
            BASE_DIR
            / "data"
            / "processed"
            / "corpus.txt"
        )

    def build_corpus(self):

        self.books_path.mkdir(
            parents=True,
            exist_ok=True
        )

        self.processed_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        texts = []

        for file_path in self.books_path.glob("*.txt"):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                texts.append(file.read())

        corpus = "\n".join(texts)

        with open(
            self.processed_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(corpus)

        print()
        print("=" * 45)
        print("          CORPUS CONSTRUIDO")
        print("=" * 45)

        print(
            f"Archivos encontrados: {len(texts)}"
        )

        print(
            f"Caracteres: {len(corpus)}"
        )

        print()
        print("Corpus guardado en:")

        print(self.processed_path)

    def load_corpus(self):

        if not self.processed_path.exists():

            print(
                "El corpus todavía no existe."
            )

            print(
                "Construyendo corpus..."
            )

            self.build_corpus()

        with open(
            self.processed_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()
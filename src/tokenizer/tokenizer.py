import re


class Tokenizer:

    def manual_tokenizer(self, text):

        """
        Tokenizador manual.
        """

        tokens = re.findall(
            r"\b\w+\b",
            text.lower(),
            flags=re.UNICODE
        )

        return tokens

    def run(
        self,
        text,
        tokenizer_type="manual"
    ):

        if tokenizer_type == "manual":

            tokens = self.manual_tokenizer(text)

        else:

            print(
                "Tipo de tokenizador no válido."
            )

            return []

        print()
        print("=" * 45)
        print("            TOKENIZADOR")
        print("=" * 45)

        print(
            f"Tipo: {tokenizer_type}"
        )

        print(
            f"Cantidad de tokens: {len(tokens)}"
        )

        print()
        print("Primeros tokens:")

        print(tokens[:30])

        return tokens